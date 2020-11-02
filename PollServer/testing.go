
package main

import (
	"fmt"
	"github.com/gorilla/mux"
	"log"
	"net/http"
	"io/ioutil"
    "io"
)


type Gateway struct {
	NetIp         string
	MacAddr       string
	Id            int
	Response      chan string
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
			fmt.Println("Gateway Offline: ", g) 
		default:
			fmt.Println(" ")
	}
}


func addGateway(gAddress, gMac string, gId int, gReq *http.Request) Gateway {
	gResponse := make(chan string)
	instance := Gateway{gAddress, gMac, gId, gResponse, gReq}
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
			value.Response <- string(body)
		}
	}
}


//io.WriteString(w, <-client.Channel //sends written response



//this is where you can check to see if the request is dead
func pollRequest(w http.ResponseWriter, r *http.Request) {

	requestAddr := r.FormValue("address")
	requestMacAddr := r.FormValue("mac-address")
	clientInstance := addGateway(requestAddr, requestMacAddr, gatewayCount, r)

	if CheckDupes(clientInstance.MacAddr) == false {
		gateways = append(gateways, clientInstance)
		gatewayCount += 1
		fmt.Println("Polling a response from: ", requestMacAddr)
		io.WriteString(w, <-clientInstance.Response)
	}else{
		fmt.Fprintf(w, "Cannot create client || Client exists ")
	}

}

//create a channel for active request, call it requestsChannel



func serverHandler(Port string) {
	fmt.Println("Control server listening on port", Port)
	myPort := fmt.Sprintf(":%s", Port)
	serverRouter := mux.NewRouter().StrictSlash(true)
	serverRouter.HandleFunc("/poll", pollRequest).Methods("POST")
    serverRouter.HandleFunc("/push/{macAddr}", pushHandler).Methods("POST")
	log.Fatal(http.ListenAndServe(myPort, serverRouter))
}

func main() {
	serverHandler("8080")
}
