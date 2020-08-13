import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:convert';
import 'Service.dart'; 
import 'package:shared_preferences/shared_preferences.dart';


class Posting {

register(String username, password, email) async {
    Map data = {
      'username': username,
      'email': password,
      'password': email,
    };

    var jsonData = null;
    SharedPreferences prefs = await SharedPreferences.getInstance();
    final network = prefs.getString('network');
    var response = await http.post(
        "$network/dtunes/auth/register/", body: data);
    //if this user gets a token, send them to the home page
    if (response.statusCode == 200) {
      jsonData = json.decode(response.body);
      print(jsonData);
      print('Successful sign in');

      return "Success"; 

      //this is to move us to the next page
      //print(jsonData['token']);
      //var auth_token = jsonData['token'];
    } else {
      return "Failure"; 
    }
  }


    //THIS IS OUR SIGN IN METHOD
signIn(String username, password) async {
  
    Map data = {
      'username': username,
      'password': password
    };

    var jsonData = null;
    //SharedPreferences  prefs = await SharedPreferences.getInstance();
    //final network = prefs.getString('network');
    var response = await http.post("http://10.0.0.153:8000/api-token-auth/", body: data);
    //if this user gets a token, send them to the home page
    if(response.statusCode == 200){
      jsonData = json.decode(response.body);
      final auth_token = jsonData['token'];
      Service.setUrlToken("http://10.0.0.153:8000", auth_token); 
    

        //prefs.setString("token", jsonData['token']);
        //print(prefs.getString("token"));
        //Service.setToken(); 
        //Navigator.push(
            //context,
            //MaterialPageRoute(builder: (context) => MainPage()));
     
      //this is to move us to the next page
      //print(jsonData['token']);
      //var auth_token = jsonData['token'];

      return "Success"; 


    }else{

       return "Failure";  
      
    }
  }


}