package main

import(
	"fmt"
	"net/http"
	"net/url"
)



func main(){
	resp, err := http.Post("http://127.0.0.1:8080/view", url.Values{"key": {"Value"}})
	if err != nil{
		log.Fatal(err)
	}
	if(resp.StatusCode == 200){
		fmt.Println("success")
	}
	if(resp.StatusCode == 400){
		fmt.Println("Failed request")
	}
}
