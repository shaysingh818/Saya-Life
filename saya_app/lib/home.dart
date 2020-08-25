import 'package:flutter/material.dart';
import 'package:flutter/painting.dart';
import './api/Service.dart';
import './models/Notifications.dart'; 
import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:convert';


class HomePage extends StatefulWidget {


  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {

  String HOST;


  /**
   * Get the current youtube API key stored in the django database to set it
   * in shared preferences
   * 
   * Might need to move this to the library.dart file
   */



  /**
   * Bottom navigation bar index selection
   */

  double charge_sum;
  String tier;
  int hcf;
  int gallons; 
  double service_total; 
  bool is_loading = true;


  Future<String> getBill() async{
    final token = Service.auth_token; 
    final network = Service.url; 


    http.Response response = await http.get(
        Uri.encodeFull("$network/billing/users/current-bill/"),
        headers: {
          "Accept":"application/json",
          "Authorization": "Token ${token} "
        }
    );

    final jsonData = json.decode(response.body);
    print(jsonData);

    setState(() {
      charge_sum = jsonData["charge_sum"];
      tier = jsonData["tier"];
      hcf = jsonData["HCF"];
      gallons = jsonData["gallons"]; 
      service_total = jsonData["service_total"]; 
      
    });

  
    return "Success!";
  }

  List<Notifications> _notifications; 

@override
  void initState(){
    super.initState();

    Service.getNotifs().then((notifications){
      
      setState(() {
        _notifications = notifications; 
        is_loading = false; 

      });
    });

    this.getBill();
   
  }


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: CustomScrollView(
        slivers: [
          SliverToBoxAdapter(
            child: Center(
        child: Column(children: [
          SizedBox(
            height: 10 ,
          ),
          Container(
            margin: EdgeInsets.all(10.0),
            decoration: BoxDecoration(
              border: Border.all(color: Colors.blue, width: 5.0), 
              color: Colors.white,
              shape: BoxShape.circle, 
              ),
            height: 270,
            child: Center(
              child: Column(children: [
                SizedBox(
                  height: 50,
                ), 
                Text(hcf.toString() + " " + "HCF", style: TextStyle(fontSize: 50, fontWeight: FontWeight.bold),),
                SizedBox(
                  height: 10,
                ), 
                Text(gallons.toString() + ' Gallons per HCF', style: TextStyle(color: Colors.black, fontSize: 17)),
                SizedBox(
                  height: 10,
                ), 
                Text(charge_sum.toString(), style: TextStyle(color: Colors.green, fontSize: 45))
              ],),
            ),
          ),
          SizedBox(
            height: 20,
          ), 

          ListTile(
            leading: Icon(
              Icons.attach_money,
              color: Colors.green, 
            ),
            title: Text("View current bill", style: TextStyle(color: Colors.black, fontWeight: FontWeight.bold)),
            subtitle: Text('View charges related to your current water usage'),
          ),
          ListTile(
            leading: Icon(
              Icons.location_city,
              color: Colors.blue, 
            ),
            title: Text("View county charges", style: TextStyle(color: Colors.black, fontWeight: FontWeight.bold)),
            subtitle: Text('View charges related to the county you reside in'),
          ),
          SizedBox(
            height: 5,
          ),
          ListTile(
            leading: Icon(
              Icons.message,
              color: Colors.blue, 
            ),
            title: Text("Messages", style: TextStyle(color: Colors.black, fontWeight: FontWeight.bold, fontSize: 20.0)),
          
          ),
         
         
          ],  
          ),
        ),
      ),
      SliverList(delegate: SliverChildBuilderDelegate(
        (BuildContext context, int index){
          Notifications notification = _notifications[index]; 
          return  Card(
            child: Column(children: [
              ListTile(
                leading: Icon(
                  Icons.message, 
                ), 
                title: Text(notification.title, style: TextStyle(fontWeight: FontWeight.bold)),
                subtitle: Text(notification.subtitle),
              )
            ],) ,
          );
        },
        childCount: _notifications == null ? 0: _notifications.length, 
      ),)
      ],
    )
    

    );
  }
}