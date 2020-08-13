import 'package:flutter/material.dart';
import 'package:flutter/painting.dart';

class PropertyPage extends StatefulWidget {


  @override
  _PropertyPageState createState() => _PropertyPageState();
}

class _PropertyPageState extends State<PropertyPage> {

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

          Card(child: Column(children: [
            Text('View your Bills'),
            ListTile(
              leading: Icon(
                Icons.money, 
              ),
              title: Text('Total paid'),
              subtitle: Text('Contact your water provider for any questions'),
            ),
            
          ],),)
         
         
          ],  
          ),
        ),
      ),
      SliverList(delegate: SliverChildBuilderDelegate(
        (BuildContext context, int index){
          return  Card(
            child: Column(children: [
              ListTile(
                leading: Icon(
                  Icons.message, 
                ), 
                title: Text('Bill For month of august', style: TextStyle(fontWeight: FontWeight.bold)),
                subtitle: Text('Your monthly bill for water usage'),
              )
            ],) ,
          );
        },
        childCount: 30, 
      ),)
      ],
    )
    

    );
  }
}