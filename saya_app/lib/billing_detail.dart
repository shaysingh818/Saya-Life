import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/painting.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import 'dart:convert';
import 'dart:io'; 
import './models/Charges.dart';  
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

   setState(() {
      tier_water_usage = jsonData["tier_water_usage"];
      service_charge_total = jsonData["service_charge_total"]; 
      total_amount = jsonData["total_amount"]; 
    });

   



    return "Success!";
  }







  List<Charges> _charges; 



  @override
  void initState(){
    super.initState();

    is_loading = true; 

    this.getArtist();

    Service.getBillCharges(pk).then((charges){
      
      setState(() {
        _charges = charges; 
        is_loading = false; 

      });
    });
 
    




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
                            trailing:  Text(total_amount, style: TextStyle(color: Colors.green, fontWeight: FontWeight.bold)), 
                          ),
                        ListTile(
                            leading: Icon(
                              Icons.monetization_on, 
                              color: Colors.blue, 
                            ), 
                            title: Text("Service Charge Amount: ", style: TextStyle(color: Colors.black, fontWeight: FontWeight.bold)),
                            trailing: Text(service_charge_total, style: TextStyle(color: Colors.green, fontWeight: FontWeight.bold)), 
                          ),
                          ListTile(
                            leading: Icon(
                              Icons.monetization_on, 
                              color: Colors.blue, 
                            ), 
                            title: Text("Tier Usage: ", style: TextStyle(color: Colors.black, fontWeight: FontWeight.bold)),
                            trailing: Text(tier_water_usage, style: TextStyle(color: Colors.green, fontWeight: FontWeight.bold)), 
                          ),
                        ],
                      )
                    ),

                     Card(
                      child: Column(
                        children: [
                          ListTile(
                            leading: Icon(
                              Icons.water_damage_rounded,  
                              color: Colors.blue, 
                            ), 
                            title: Text("Water Usage Charge Chart ", style: TextStyle(color: Colors.black, fontWeight: FontWeight.bold)),
                            trailing: Icon(
                              Icons.water_damage, 
                              color: Colors.grey, 
                            )
                          ),
                        Card(
                          color: Colors.lightBlue[100],
                          child: ListTile(
                            title: Text("Tier 1 ~ Low Volume ", style: TextStyle(color: Colors.black, fontWeight: FontWeight.normal)),
                            trailing: Text("9 HCF/9.49", style: TextStyle(color: Colors.black, fontWeight: FontWeight.bold)), 
                          ),
                        ),
                         Card(
                          color: Colors.lightBlue[200],
                          child: ListTile(
                            title: Text("Tier 2 ~ Low Volume ", style: TextStyle(color: Colors.black, fontWeight: FontWeight.normal)),
                            trailing: Text("18 HCF/10.49", style: TextStyle(color: Colors.black, fontWeight: FontWeight.bold)), 
                          ),
                        ),
                         Card(
                          color: Colors.lightBlue[300],
                          child: ListTile(
                            title: Text("Tier 3 ~ High Volume ", style: TextStyle(color: Colors.black, fontWeight: FontWeight.normal)),
                            trailing: Text("21 HCF/10.49", style: TextStyle(color: Colors.black, fontWeight: FontWeight.bold)), 
                          ),
                        ),
                         Card(
                          color: Colors.lightBlue[400],
                          child: ListTile(
                            title: Text("Tier 4 ~ High Volume ", style: TextStyle(color: Colors.black, fontWeight: FontWeight.normal)),
                            trailing: Text("26 HCF/12.49", style: TextStyle(color: Colors.black, fontWeight: FontWeight.bold)), 
                          ),
                        )

                         
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
                        
                        
                        ],
                      )
                    ),

                    

                   
                  ],
                )
                
              ),

              

            ),

          SliverList(delegate: SliverChildBuilderDelegate(
            (BuildContext context, int index){
              Charges charge = _charges[index]; 
              return  Card(
                child: Column(children: [
                  ListTile(
                  
                    leading: Icon(
                      Icons.message, 
                    ), 
                    title: Text(charge.title, style: TextStyle(fontWeight: FontWeight.bold)),
                    subtitle: Text('Total: ' + charge.chargeAmount ),
                  )
                ],) ,
              );
            },
            childCount: _charges == null ? 0: _charges.length, 
          ),), 
            
          ],
        )
    );
  }
}