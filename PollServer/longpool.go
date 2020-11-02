package main

import(
	"fmt"
	"github.com/gorilla/mux"
	"net/http"
	"log"
	"io/ioutil"
	"io"
	//"time"
)

type Gateway struct{
	NetIp string
	Id int
	Channel chan string
	Status bool
	MacAddr string
	ClientRequest *http.Request
}

//gateways
var clients []Gateway
var ClientCount = 0
var ServerIp = "http://127.0.0.1:8080"

func(g *Gateway) CheckMac(address string) bool{
	status := false
	if g.MacAddr == address {
		status = true
	}
	return status
}


func checkStatus(w http.ResponseWriter, r *http.Request){
	for _, value := range clients {
		fmt.Println(value.ClientRequest.Context())
	}
}


func CheckDupes(address string) bool{
	status := false
	for _, value := range clients{
		if value.CheckMac(address) == true {
			status = true
		}
	}
	return status
}

func AddClient(Address, MacAddress string, UnitId int, Online bool, CRequest *http.Request) Gateway{
	channel := make(chan string)
	instance := Gateway{Address,UnitId,channel,Online,MacAddress,CRequest}
	return instance
}

//check to see if client is still making active request


//method to write response to all clients
func PushAll(w http.ResponseWriter, req *http.Request){
	for _, value := range clients{
		formatUrl := fmt.Sprintf("%s/push/%s", ServerIp, value.MacAddr)
		resp, err := http.Get(formatUrl)
		if err != nil{
			log.Fatal(err)
		}
		if resp.StatusCode == 200 {
			fmt.Println("Pushed Gateway:", value.MacAddr)
		}

	}

	fmt.Fprintf(w, "Writing to all devices")
}

func IndexDeviceMac(searchAddress string) int{
	index := 0
	var foundIndex int
	for _, value := range clients{
		if value.MacAddr == searchAddress {
			fmt.Println("Found device")
			foundIndex = index
		}
		index += 1
	}
	return foundIndex
}

func ViewGateways(w http.ResponseWriter, req *http.Request){
	for _, value := range clients{
		fmt.Println(value)
	}
}

//write response to individual gateway
func PushHandler(w http.ResponseWriter, req *http.Request){
	params := mux.Vars(req)
	mac := params["mac_address"]
	index := IndexDeviceMac(mac)
	body, err := ioutil.ReadAll(req.Body)
	if err != nil{
		w.WriteHeader(400)
	}
	clients[index].Channel <-string(body)
}


//send client mac address and IP to request
//This shouldn't write to a channel with a dupe Mac address
func pollResponse(w http.ResponseWriter, r *http.Request){

	Addr := r.FormValue("address")
	MacAddr := r.FormValue("mac-address")


	createClient := AddClient(Addr,MacAddr, ClientCount, true, r)
	if CheckDupes(createClient.MacAddr) == true {
		fmt.Fprintf(w, "Cannot add client")
	}else{
		clients = append(clients, createClient)
		ClientCount += 1
		io.WriteString(w, <-createClient.Channel)
	}
}

func controlHandler(Port string){
	fmt.Println("Control server listening on port", Port)
	myPort := fmt.Sprintf(":%s", Port)
	myRouterTwo := mux.NewRouter().StrictSlash(true)
	myRouterTwo.HandleFunc("/view", ViewGateways).Methods("GET")
	myRouterTwo.HandleFunc("/poll", pollResponse).Methods("POST")
	myRouterTwo.HandleFunc("/push/{mac_address}", PushHandler).Methods("GET")
	myRouterTwo.HandleFunc("/patch", PushAll).Methods("GET")
	myRouterTwo.HandleFunc("/check", checkStatus).Methods("GET")
	log.Fatal(http.ListenAndServe(myPort, myRouterTwo))

}

func main(){
	controlHandler("8081")

}
