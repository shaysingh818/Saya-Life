# Poll a response
Send a request as client gateway, server will hold the response and keep the connection alive. If a duplicate client makes a request, server will close previous request

HTTP POST
http://127.0.0.1:8080/poll

PARAMS
{
	mac-address: <MAC ADDR/Client Identifier>
}

# PUSH a response / Send gateway command

HTTP POST
http://127.0.0.1:8080/push/{MACADDR}


# SEND report to gateway

HTTP POST
http://127.0.0.1:8080/nano/{MACADDR}

PARAMS

```
{
	   "TotalFlow":    "11812.97932",
	        "Flow":       "15.32200",
	    "FlowRate":        "0.25473",
	 "InstantFlow":        "0.00000",
	"SupplyWaterTemperature":       "83.84000",
	"BackWaterTemperature":        "0.00000",
	"BackWaterPressure":        "0.00000",
	"SupplyWaterPressure":       "80.05572",
	 "CaptureTime":              "2020/10/21-15:40:37",
	"MeterLocalTime":              "2020/10/21-15:40:37",
	  "ValveState":              "1",
	  "BatteryLow":           "true",
	"TemperatureSensorFunctional":           "true",
	"FlowSensorFunctional":           "true",
	"ExternalPower":           "true",
	"OpenValveError":          "false",
	"CloseValveError":          "false",
	"BackupBatteryLow":          "false",
	 "MeterNumber":              "18110365",
	          "Id":            "373",
	"SendInterval":           "3600"
}
```

