import 'package:flutter/material.dart';
import 'package:flutter/painting.dart';

class StatesPage extends StatefulWidget {


  @override
  _StatesPageState createState() => _StatesPageState();
}

class _StatesPageState extends State<StatesPage> {

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

  TextEditingController songsearchController = new TextEditingController();


  _buildSongSearchComposer(){
    return Container(
      padding: EdgeInsets.symmetric(horizontal: 8.0),
      height: 50,
      margin: EdgeInsets.symmetric(horizontal: 10.0),
      color: Colors.grey[300],
      child: Row(
        children: <Widget>[
          IconButton(
            icon: Icon(Icons.music_note, color: Colors.red),
          ),
          Expanded(
              child: TextField(
                controller: songsearchController,
                decoration: InputDecoration.collapsed(
                    hintText: 'Search States'
                ),

              )

          ),
          IconButton(
            icon: Icon(Icons.search, color: Colors.red),
            onPressed: (){
              setState(() {
                
                

                
              });
            },
          ),
        ],
      ),



    );
  }


   TextEditingController nameController = new TextEditingController();


/**
 * 
 * Text field component for name of network
 * 
 */

  _buildNameComposer(){
    return Container(
      padding: EdgeInsets.symmetric(horizontal: 8.0),
      height: 50,
      margin: EdgeInsets.symmetric(horizontal: 10.0),
      color: Colors.grey[300],
      child: Row(
        children: <Widget>[
          IconButton(
            icon: Icon(Icons.music_note, color: Colors.red),
          ),
          Expanded(
              child: TextField(
                controller: nameController,
                decoration: InputDecoration.collapsed(
                    hintText: 'Input State'
                ),

              )

          ),
          IconButton(
            icon: Icon(Icons.add, color: Colors.red),
            onPressed: (){
              setState(() {

              });
            },
          ),
        ],
      ),



    );
  }

final _formKey = GlobalKey<FormState>();

TextEditingController networkController = new TextEditingController();
    _buildNetworkComposer(){
    return Container(
      padding: EdgeInsets.symmetric(horizontal: 8.0),
      height: 50,
      margin: EdgeInsets.symmetric(horizontal: 10.0),
      color: Colors.grey[300],
      child: Row(
        children: <Widget>[
          IconButton(
            icon: Icon(Icons.music_note, color: Colors.red),
          ),
          Expanded(
              child: TextField(
                controller: networkController,
                decoration: InputDecoration.collapsed(
                    hintText: 'Input State Code'
                ),

              )

          ),
          IconButton(
            icon: Icon(Icons.add, color: Colors.red),
            onPressed: (){
              setState(() {




              });
            },
          ),
        ],
      ),



    );
  }

    void showBottomSheet(){
    showModalBottomSheet(context: context, builder: (context){
      return Column(
        children: <Widget>[
          Container(
            color: Colors.white, 
            
              child: Column(
                children: <Widget>[
                  ListTile(
                    title: Text('Add a State', style: TextStyle(fontWeight: FontWeight.bold, color: Colors.black))
                  ),
                  Form(
                    key: _formKey,
                    child: Column(
                      children: <Widget>[
                        _buildNameComposer(),
                        SizedBox(
                          height: 20,
                        ),
                        _buildNetworkComposer(),
                      ],
                    ),
                  ),
                  SizedBox(
                    height: 30,

                  ),
                  GestureDetector(
                    onTap: (){
                     


                    },
                    child:  Container(
                      height: 50,
                      width: 200,
                      padding: EdgeInsets.symmetric(horizontal: 20.0),
                      decoration: BoxDecoration(
                          color: Colors.red,
                          borderRadius: BorderRadius.circular(15.0)
                      ),
                      child: Center(
                        child: Text(
                            'Add State',
                            style: TextStyle(
                                fontWeight: FontWeight.bold,
                                color: Colors.white,
                                fontSize: 16
                            )
                        ),
                      ),

                    ),
                  )

                ],
              )
          ),
        ],
      );
    });

  }
  







  @override
  Widget build(BuildContext context) {
    return Scaffold(
       appBar: AppBar(
          title: Text('Locations'),
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
            SizedBox(
              height: 10,
            ),
            _buildSongSearchComposer(), 
           
          ],),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        backgroundColor: Colors.red,
        onPressed: () {
          setState(() {
            showBottomSheet();
           
          });
        },
        child: Icon(Icons.add),
      ) ,

    );
  }
}