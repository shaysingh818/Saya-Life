package main

import(
	//"fmt"
	//"github.com/gorilla/mux"
	//"net/http"
	//"log"
	//"io/ioutil"
	//"io"
	"time"
)

NanoAddr := "tcp://127.0.0.1:8888"

type Report struct {
	TotalFlow float64
	Flow float64
	FlowRate float64
	InstantFlow float64
	SupplyWaterTemp float64
	BackWaterTemp float64
	BackWaterPressure float64
	SupplyWaterPressure float64
	BackWaterTemp float64
	CaptureTime float64 //Date field time.Time
	MeterLocalTime float64 //date field time.Time
	ValveState int32
	BatteryLow bool
	TemperatureSensorFunctional bool
	FlowSensorFunctional bool
	ExternalPower bool
	OpenValveError bool
	CloseValveError bool
	BackupBatteryLow bool
	MeterNumber int32
	MeterId int32
	SendInterval int32
}




