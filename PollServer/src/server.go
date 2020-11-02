package main

import(
	"fmt"
	"github.com/gorilla/mux"
	"log"
	"net/http"
	"io/ioutil"
	"io"

)



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

	requestAddr := r.FormValue("address")
	requestMacAddr := r.FormValue("mac-address")
	clientInstance := addGateway(requestAddr, requestMacAddr, gatewayCount, r)

	if CheckDupes(clientInstance.MacAddr) == false {
		gateways = append(gateways, clientInstance)
		gatewayCount += 1
		fmt.Println("Polling a response from: ", requestMacAddr)
		io.WriteString(w, <-clientInstance.Channel)
	}else{
		fmt.Fprintf(w, "Cannot create client || Client exists ")
	}


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
	log.Fatal(http.ListenAndServe(myPort, serverRouter))
}

func main() {
	serverHandler("8080")
}
