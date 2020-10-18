import 'package:shared_preferences/shared_preferences.dart';
import '../models/Bill.dart';
import '../models/Charges.dart'; 
import '../models/Notifications.dart';
import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:convert';


class Service{

  static String url; 
  static String auth_token; 

  static setUrlToken(final_url, token) async {
    url = final_url; 
    auth_token = token; 

    print(url);
    print(token);

  }

  static Future<List<Bill>> getBills() async {
    try {
      final response = await http.get('$url/billing/users/bills/', headers: {
         "Accept":"application/json",
          "Authorization": "Token $auth_token"

      });
      if(response.statusCode == 200){
        final List<Bill> bills = billFromJson(response.body);
        return bills;
      }else{
        return List<Bill>(); 
      }

    }catch(e){
      return List<Bill>(); 

    }

  }

  static Future<List<Charges>> getBillCharges(int pk) async {
    try {
      final response = await http.get('$url/billing/users/bill-charges/$pk/', headers: {
         "Accept":"application/json",
          "Authorization": "Token $auth_token"

      });
      if(response.statusCode == 200){
        final List<Charges> charges = chargesFromJson(response.body);
        return charges;
      }else{
        return List<Charges>(); 
      }

    }catch(e){
      return List<Charges>(); 
    }

  }

    static Future<List<Notifications>> getNotifs() async {
    try {
      final response = await http.get('$url/billing/users/notifications/', headers: {
         "Accept":"application/json",
          "Authorization": "Token $auth_token"

      });
      if(response.statusCode == 200){
        final List<Notifications> notifications = notificationsFromJson(response.body);
        return notifications;
      }else{
        return List<Notifications>(); 
      }

    }catch(e){
      return List<Notifications>(); 

    }

  }

}