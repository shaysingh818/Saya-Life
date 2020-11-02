package main

import(
	"fmt"
	"net/http"

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


