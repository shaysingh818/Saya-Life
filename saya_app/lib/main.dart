import 'package:flutter/material.dart';
import 'login.dart'; 
void main() async {

  WidgetsFlutterBinding.ensureInitialized();
  runApp(MyApp());

}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {

    return MaterialApp(
      theme: ThemeData(
        primaryColor: Colors.blue[400],
      ),
      title: "Saya Billing",
      home: Scaffold(

        body: LoginPage(),
      ),
    );
  }
}
