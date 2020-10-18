import 'package:flutter/material.dart';
import 'package:flutter/painting.dart';
import './models/Bill.dart'; 
import './api/Service.dart';
import 'billing_detail.dart'; 

class BillingPage extends StatefulWidget {


  @override
  _BillingPageState createState() => _BillingPageState();
}

class _BillingPageState extends State<BillingPage> {

  String HOST;

  List<Bill> _bills; 

  bool is_loading = false;

  @override
  void initState(){
    super.initState(); 
    is_loading = true; 
   
    Service.getBills().then((bills){
      
      setState(() {
        _bills = bills; 
        is_loading = false; 

      });
    });
  }

  /**
   * Get the current youtube API key stored in the django database to set it
   * in shared preferences
   * 
   * Might need to move this to the library.dart file
   */



  /**
   * Bottom navigation bar index selection
   */

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: CustomScrollView(
        slivers: [
          SliverToBoxAdapter(
            child: Center(
        child: Column(children: [
         
         
         
          ],  
          ),
        ),
      ),
      SliverList(delegate: SliverChildBuilderDelegate(
        (BuildContext context, int index){
          Bill bill = _bills[index]; 
          return  Card(
            child: Column(children: [
              ListTile(
                onTap: (){
                  Navigator.push(
                      context,
                  MaterialPageRoute(builder: (context) => BillingDetailPage(pk: bill.id)));
                },
                leading: Icon(
                  Icons.message, 
                ), 
                title: Text(bill.dateBillPrepared.toString(), style: TextStyle(fontWeight: FontWeight.bold)),
                subtitle: Text('Total: ' + bill.totalAmount.toString() + " " + "Service charge total: " + bill.serviceChargeTotal.toString()),
              )
            ],) ,
          );
        },
        childCount: _bills == null ? 0: _bills.length, 
      ),)
      ],
    )
    

    );
  }
}