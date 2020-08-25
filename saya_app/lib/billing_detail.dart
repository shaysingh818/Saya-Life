import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/painting.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import 'dart:convert';
import 'dart:io'; 
import './models/Bill.dart';  
import './api/Posting.dart'; 
import './api/Service.dart';

class BillingDetailPage extends StatefulWidget {

  final pk;

  BillingDetailPage({Key key, @required this.pk}) : super(key: key);

  @override
  _BillingDetailPageState createState() => _BillingDetailPageState(pk);
}

class _BillingDetailPageState extends State<BillingDetailPage> {

  Posting _action = Posting(); 

  int pk;

  _BillingDetailPageState(this.pk);

  bool is_following = false;

  String HOST;

  String tier_water_usage;
  String service_charge_total;
  String total_amount;
  bool is_loading = true;


  Future<String> getArtist() async{
    final token = Service.auth_token; 
    final network = Service.url; 
    HOST = network;

    http.Response response = await http.get(
        Uri.encodeFull("$network/billing/users/bill/$pk/?format=json"),
        headers: {
          "Accept":"application/json",
          "Authorization": "Token ${token} "
        }
    );

    final jsonData = json.decode(response.body);
    print(jsonData);
/**
 *  setState(() {
      tier_water_usage = jsonData["tier_water_usage"];
      print(image_url); 
      name = jsonData["name"];
      followstatus = jsonData["follow_status"];
    });
 */
   



    return "Success!";
  }







  //List<Playlists> _playlists; 



  @override
  void initState(){
    super.initState();

    is_loading = true; 

    //this.getArtist();
   
   /**
    * Service.getPlaylists().then((playlists){
      setState(() {
        _playlists = playlists; 
        is_loading = false; 
      });
    });
    */

    




  }


  @override
  Widget build(BuildContext context) {
    return Scaffold(
     
        appBar: AppBar(
          backgroundColor: Colors.white,
          title: Text("Testing"),
          actions: <Widget>[
            IconButton(
              icon: Icon(
                Icons.add,
              ),
              onPressed: () {
                //addPhotoSheet();
              },
            ),
          ],
        ),
        body: CustomScrollView(
          slivers: <Widget>[
            SliverToBoxAdapter(
              child: Container(
                child: Column(
                  children: [
                    Card(
                      child: Column(
                        children: [
                          ListTile(
                            leading: Icon(
                              Icons.monetization_on, 
                              color: Colors.blue, 
                            ), 
                            title: Text("Total amount due: ", style: TextStyle(color: Colors.black, fontWeight: FontWeight.bold)),
                            trailing:  Text("123 Dollars", style: TextStyle(color: Colors.green, fontWeight: FontWeight.bold)), 
                          ),
                        ListTile(
                            leading: Icon(
                              Icons.monetization_on, 
                              color: Colors.blue, 
                            ), 
                            title: Text("Service Charge Amount: ", style: TextStyle(color: Colors.black, fontWeight: FontWeight.bold)),
                            trailing: Text("123 Dollars", style: TextStyle(color: Colors.green, fontWeight: FontWeight.bold)), 
                          ),
                          ListTile(
                            leading: Icon(
                              Icons.monetization_on, 
                              color: Colors.blue, 
                            ), 
                            title: Text("Water Usage Charge Amount: ", style: TextStyle(color: Colors.black, fontWeight: FontWeight.bold)),
                            trailing: Text("123 Dollars", style: TextStyle(color: Colors.green, fontWeight: FontWeight.bold)), 
                          ),
                        ],
                      )
                    ),

                    Card(
                      child: Column(
                        children: [
                          ListTile(
                            leading: Icon(
                              Icons.monetization_on, 
                              color: Colors.blue, 
                            ), 
                            title: Text("County service charges ", style: TextStyle(color: Colors.black, fontWeight: FontWeight.bold)),
                            trailing: Icon(
                              Icons.info, 
                              color: Colors.grey, 
                            )
                          ),
                        ListTile(
                            title: Text("Service Charge Amount: ", style: TextStyle(color: Colors.black, fontWeight: FontWeight.normal)),
                            trailing: Text("123 Dollars", style: TextStyle(color: Colors.green, fontWeight: FontWeight.bold)), 
                          ),
                          ListTile(
                           
                            title: Text("Water Usage Charge Amount: ", style: TextStyle(color: Colors.black)),
                            trailing: Text("123 Dollars", style: TextStyle(color: Colors.green, fontWeight: FontWeight.bold)), 
                          ),
                        ],
                      )
                    ),

                  ],
                )
                
              ),

            ),
            
          ],
        )
    );
  }
}