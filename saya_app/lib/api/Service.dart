import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:convert';
import '../models/States.dart';




// To parse this JSON data, do
//
//     final artist = artistFromJson(jsonString);


class Service {



  static String url; 
  static String auth_token; 

  static setUrlToken(final_url, token) async {
    url = final_url; 
    auth_token = token; 

    print(url);
    print(token);

  }



/******************************************************************
   * 
   * THIS IS FOR THE ARTIST MODEL
   *************************************************************/ 


static Future<List<States>> getArtists() async {
    try {
      final response = await http.get('$url/billing/states/states/', headers: {
         "Accept":"application/json",
          "Authorization": "Token $auth_token"

      });
      if(response.statusCode == 200){
        final List<States> states = statesFromJson(response.body);
        return states;
      }else{
        return List<States>(); 
      }

    }catch(e){
      return List<States>(); 

    }

  }

 


}