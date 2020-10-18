// To parse this JSON data, do
//
//     final charges = chargesFromJson(jsonString);

import 'dart:convert';

List<Charges> chargesFromJson(String str) => List<Charges>.from(json.decode(str).map((x) => Charges.fromJson(x)));

String chargesToJson(List<Charges> data) => json.encode(List<dynamic>.from(data.map((x) => x.toJson())));

class Charges {
    Charges({
        this.title,
        this.chargeAmount,
        this.id,
    });

    String title;
    String chargeAmount;
    int id;

    factory Charges.fromJson(Map<String, dynamic> json) => Charges(
        title: json["title"],
        chargeAmount: json["charge_amount"],
        id: json["id"],
    );

    Map<String, dynamic> toJson() => {
        "title": title,
        "charge_amount": chargeAmount,
        "id": id,
    };
}