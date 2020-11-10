package main

import(
	"os"
	"time"
	"fmt"
	//Mangos NNG implementation
	"nanomsg.org/go-mangos"
	"nanomsg.org/go-mangos/protocol/pub"
	"nanomsg.org/go-mangos/transport/ipc"
	"nanomsg.org/go-mangos/transport/tcp"
)

var nano_addr = "tcp://127.0.0.1:8888"

//Report struct to parse JSON request
type Report struct {
	TotalFlow string `json:"TotalFlow"`
	Flow string `json:"Flow"`
	FlowRate string `json:"FlowRate"`
	InstantFlow string `json:"InstantFlow"`
	SupplyWaterTemp string `json:"SupplyWaterTemp"`
	BackWaterTemp string `json:"BackWaterTemperature"`
	BackWaterPressure string `json:"BackWaterPressure"`
	SupplyWaterPressure string `json:"SupplyWaterPressure"`
	CaptureTime string `json:"CaptureTime"`
	MeterLocalTime string `json:"MeterLocalTime"`
	ValveState string `json:"ValveState"`
	BatteryLow string `json:"BatteryLow"`
	TemperatureSensorFunctional string `json:"TemperatureSensorFunctional"`
	FlowSensorFunctional string `json:"FlowSensorFunctional"`
	ExternalPower string `json:"ExternalPower"`
	OpenValveError string `json:"OpenValveError"`
	CloseValveError string `json:"CloseValveError"`
	BackupBatteryLow string `json:"BackupBatteryLow"`
	MeterNumber string `json:"MeterNumber"`
	MeterId string `json:"Id"`
	SendInterval string `json:"SendInterval"`
}

//socket for pub
var sock mangos.Socket
var err error

func die(format string, v ...interface{}) {
	fmt.Fprintln(os.Stderr, fmt.Sprintf(format, v...))
	os.Exit(1)
}
//get date of push
func date() string {
	return time.Now().Format(time.ANSIC)
}
//publish socket
func nanoServer(){
	if sock, err = pub.NewSocket(); err != nil {
		die("can't get new pub socket: %s", err)
	}
	sock.AddTransport(ipc.NewTransport())
	sock.AddTransport(tcp.NewTransport())
	if err = sock.Listen(nano_addr); err != nil {
		die("can't listen on pub socket: %s", err.Error())
	}
	fmt.Println("NANO SERVICE STARTED: ", nano_addr)
}

//send report (macAddr, report) as parameters
func (g *Gateway) sendReport(report, macAddr string){
	fmt.Printf("SERVER: PUBLISHING REPORT %s: %s\n", macAddr, report)
	if err = sock.Send([]byte(report)); err != nil {
		die("Failed publishing: %s", err.Error())
	}
	time.Sleep(time.Second)
}
