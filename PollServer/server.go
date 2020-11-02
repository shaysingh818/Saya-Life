package main

import (
	"fmt"
	"github.com/gorilla/mux"
	"log"
	"net/http"
	"io/ioutil"
    //"io"
	"time"
)


type Gateway struct {
	NetIp         string
	MacAddr       string
	Id            int
	Channel       chan string
	ClientRequest *http.Request
}


var gateways []Gateway
var gatewayCount = 0
var host = "http://127.0.0.1:8080"

func (g *Gateway) CheckMac(address string) bool {
	status := false
	if g.MacAddr == address {
		status = true
	}
	return status
}

//throw in a mac address, return gateway
func getGateway(macAddress string) Gateway {
	for _, value := range gateways{
		if value.MacAddr == macAddress {
			return value
		}
	}
	return gateways[1]
}

func CheckDupes(address string) bool {
	status := false
	for _, value := range gateways {
		if value.CheckMac(address) == true {
			status = true
		}
	}
	return status
}


func (g *Gateway) checkRequest(){
	select{
		case <-g.ClientRequest.Context().Done():
			fmt.Println("GW DISCONNECT: ", g)
			var test = <-g.ClientRequest.Context().Done()
			fmt.Println(test) 
		default:
			fmt.Println("All Good")
	}
}

func checkAll(){
	for _, value := range gateways{
		value.checkRequest()
	}
}

func addGateway(gAddress, gMac string, gId int, gReq *http.Request) Gateway {
	gChannel := make(chan string)
	instance := Gateway{gAddress, gMac, gId, gChannel, gReq}
	return instance
}


func pushHandler(w http.ResponseWriter, req *http.Request){
	params := mux.Vars(req)

	body, err := ioutil.ReadAll(req.Body)

	if err != nil {
		w.WriteHeader(400)
	}

	mac := params["macAddr"]
	for _, value := range gateways{
		if value.MacAddr == mac {
			fmt.Println("Pushing to: ", mac)
			value.Channel <- string(body)
		}
	}
}

//this is where you can check to see if the request is dead
func pollRequest(w http.ResponseWriter, r *http.Request) {

	//requestAddr := r.FormValue("address")
	//requestMacAddr := r.FormValue("mac-address")
	//clientInstance := addGateway(requestAddr, requestMacAddr, gatewayCount, r)

	select{
		case <-time.After(10 * time.Second):
			w.Write([]byte("request processed"))

		case <-r.Context().Done():
			fmt.Println("Request cancelled")
	}

	/**
	if CheckDupes(clientInstance.MacAddr) == false {
		gateways = append(gateways, clientInstance)
		gatewayCount += 1
		fmt.Println("Polling a response from: ", requestMacAddr)
		io.WriteString(w, <-clientInstance.Channel)
	}else{
		fmt.Fprintf(w, "Cannot create client || Client exists ")
	}

	*/

}

func ViewGateways(w http.ResponseWriter, req *http.Request){
    for _, value := range gateways{
        fmt.Println(value)
    }
}



func serverHandler(Port string) {
	fmt.Println("Control server listening on port", Port)
	myPort := fmt.Sprintf(":%s", Port)
	serverRouter := mux.NewRouter().StrictSlash(true)
	serverRouter.HandleFunc("/poll", pollRequest).Methods("POST")
    serverRouter.HandleFunc("/push/{macAddr}", pushHandler).Methods("POST")
    serverRouter.HandleFunc("/view", ViewGateways).Methods("GET")
	go log.Fatal(http.ListenAndServe(myPort, serverRouter))
}

func main() {
	serverHandler("8080")
}
