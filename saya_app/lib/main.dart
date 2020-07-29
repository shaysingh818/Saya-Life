import 'package:flutter/material.dart';
import 'base_page.dart'; 


void main() async {

  WidgetsFlutterBinding.ensureInitialized();
  runApp(MyApp());

}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {

    return MaterialApp(
      theme: ThemeData(
        primaryColor: Colors.red,
          bottomSheetTheme: BottomSheetThemeData(backgroundColor: Colors.white)
      ),
      title: "Saya API",
      home: Scaffold(

        body: BasePage(),
      ),
    );
  }
}