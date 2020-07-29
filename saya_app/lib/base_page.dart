import 'package:flutter/material.dart';
import 'package:flutter/painting.dart';
import 'states.dart';

class BasePage extends StatefulWidget {


  @override
  _MainPageState createState() => _MainPageState();
}

class _MainPageState extends State<BasePage> {

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
      appBar: AppBar(
          title: Text('Saya API'),
          backgroundColor: Colors.red,
          actions: <Widget>[
            IconButton(
              icon: Icon(
                Icons.add,
                color: Colors.white,
              ),
              onPressed: (){
                setState(() {

                 
                });
              },
            )
          ],
        ),
      body: Center(
        child: Container(
          child: Column(children: [
            Text('Dashboard'), 
            
           
          ],),
        ),
      ),
      drawer: Drawer(
        child: Container(
          color: Colors.white,
          child: ListView(

            children: <Widget>[
              DrawerHeader(
                child: ListView(
                  children: <Widget>[
                    ListTile(
                     
                      title: Text('Saya API', style: TextStyle(color: Colors.white, fontSize: 20), ),
                      subtitle: Text('By: xXDiffusionXx', style: TextStyle(color: Colors.white),),

                    ),
                  ],

                ),
                decoration: BoxDecoration(
                  color: Colors.red,
                ),
              ),
              ListTile(
                onTap: (){
                  setState(() {
                     Navigator.push(
                        context,
                        MaterialPageRoute(builder: (context) => BasePage()));
                   
                  });

                },
                leading: Icon(
                  Icons.map,
                  color: Colors.red,
                ),
                title: Text('Dashboard', style: TextStyle(color: Colors.black)),
              ),
              ListTile(
                onTap: (){
                  setState(() {
                     Navigator.push(
                        context,
                        MaterialPageRoute(builder: (context) => StatesPage()));
                   
                  });
                },
                leading: Icon(
                  Icons.local_drink,
                  color: Colors.red,
                ),
                title: Text('Locations', style: TextStyle(color: Colors.black)),
              ),
              ListTile(
                onTap: (){
                  setState(() {
                  
                  });
                },
                leading: Icon(
                  Icons.attach_money,
                  color: Colors.red,
                ),
                title: Text('Analytics', style: TextStyle(color: Colors.black)),
              ),
              ListTile(
                onTap: (){
                  setState(() {
                    
                  });
                },
                leading: Icon(
                  Icons.account_circle,
                  color: Colors.red,
                ),
                title: Text('Users', style: TextStyle(color: Colors.black)),
              ),
              ListTile(
                onTap: (){
                  setState(() {
                  
                  });
                },
                leading: Icon(
                  Icons.router,
                  color: Colors.red,
                ),
                title: Text('Endpoints', style: TextStyle(color: Colors.black)),
              ),
              ListTile(
                onTap: () {
                  setState(() {
                    Navigator.pop(context);
                    Navigator.pop(context);
                    Navigator.pop(context);
                  });


                },
                leading: Icon(
                  Icons.arrow_back,
                  color: Colors.red,
                ),
                title: Text('Sign Out', style: TextStyle(color: Colors.red)),
              )
            ],
          ) ,
        )
      ),
      

    );
  }
}