/**
Author: Shalin Singh
Questions/Contact: 630-699-9717
Github: github.com/shaysingh

Purpose: Get reports from our meter gateways, perform data conversions and forward them to other backend services through nanomsg. Server provides an interface for other backend services to control the meter gateways


*/


package main

import(
	"fmt"
	"github.com/gorilla/mux"
	"log"
	"net/http"
	"io/ioutil"
	"io"
	"encoding/json"
)



//Gateway objects, Contains the IP, Mac Address, ID, Channel for holding responses and Client Request
type Gateway struct {
	NetIp         string
	MacAddr       string
	Id            int
	Channel       chan string
	ClientRequest *http.Request
}

/**
var gateways is a map of Client Gateway objects
Access the elements of the map by doing the following

//create gateway with UNIQUE mac address identifer
gateways[mac_addr] = Gateway{
			Ip,
			MacAddr,
			Id, 
			Channel, 
			ClientRequest}

Example:
gateways["DF:76:B0:DD:C4:D6"] --> returns Gateway object
fmt.Println(gateways["DF:76:B0:DD:C4:D6"]) returns Gateway Object

*/
var gateways = make(map[string]Gateway)
var gatewayCount = 0
var host = "http://127.0.0.1:8080"

//checks to see if request is active in gateway
//gateway struct holds request that was sent, you can monitor the status
func (g *Gateway) checkRequest() bool{
	var status bool = true
	select{
	   case <-g.ClientRequest.Context().Done():
		var test = <-g.ClientRequest.Context().Done()
		fmt.Println(test)
		status = false
	   default:
		status = true
	}
	return status
}


//Gets an IP/Remote addr from a HTTP request
func GetIP(r *http.Request) string {
	forwarded := r.Header.Get("X-FORWARDED-FOR")
	if forwarded != "" {
		return forwarded
	}
	return r.RemoteAddr
}

//nanomsmg route for gateway
func gatewayComm(w http.ResponseWriter, req *http.Request){
	var r Report
	params := mux.Vars(req)
	indexMac := params["macAddr"]
	if val, ok := gateways[indexMac]; ok {
		//throw the response into a report struct
		err := json.NewDecoder(req.Body).Decode(&r)
		if err != nil {
			http.Error(w, err.Error(), http.StatusBadRequest)
			return
		}
		//decode it as string
		out, err := json.Marshal(r)
		if err != nil{
			panic(err)
		}
		//send the report
		val = gateways[indexMac]
		val.sendReport(string(out), val.MacAddr)
	}

	fmt.Fprintf(w, "Report: %v", r)
}

//push response to a gateway, input mac address as parameter
func pushHandler(w http.ResponseWriter, req *http.Request){
	params := mux.Vars(req)
	body, err := ioutil.ReadAll(req.Body)

	if err != nil {
		w.WriteHeader(400)
	}
	mac := params["macAddr"]
	gateways[mac].Channel <- string(body)
	fmt.Println("Pushed to: ", gateways[mac])
}


//Poll a response --> send response to server, save response for server push
func pollRequest(w http.ResponseWriter, r *http.Request) {
	//gateway channel, {Holds the responses}
	gChan := make(chan string)
	requestAddr := GetIP(r)
	requestMacAddr := r.FormValue("mac-address")
	//check if there is an active gateway with this mac address
	if gateways[requestMacAddr].MacAddr == requestMacAddr {
		gateways[requestMacAddr].Channel <- "Disconnecting existing connection"
		delete(gateways, requestMacAddr)
	}
	//create a client instance for the gateway
	gateways[requestMacAddr] = Gateway{requestAddr, requestMacAddr, gatewayCount, gChan, r}
	connectionMessage := fmt.Sprintf("Received connection from %v : %v", requestAddr, requestMacAddr)
	fmt.Println(connectionMessage)
	io.WriteString(w, <-gateways[requestMacAddr].Channel)
}


//routes for the server, look at postman documentation for more info
func serverHandler(Port string) {
	fmt.Println("Control server listening on port", Port)
	myPort := fmt.Sprintf(":%s", Port)
	serverRouter := mux.NewRouter().StrictSlash(true)
	serverRouter.HandleFunc("/poll", pollRequest).Methods("POST")
	serverRouter.HandleFunc("/push/{macAddr}", pushHandler).Methods("POST")
	serverRouter.HandleFunc("/nano/{macAddr}", gatewayComm).Methods("POST")
	log.Fatal(http.ListenAndServe(myPort, serverRouter))
}

func main() {
	//nano socket listens as goroutine in the backround
	go nanoServer()
	serverHandler("8080")
}
