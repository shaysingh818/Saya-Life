// To parse this JSON data, do
//
//     final states = statesFromJson(jsonString);

import 'dart:convert';

List<States> statesFromJson(String str) => List<States>.from(json.decode(str).map((x) => States.fromJson(x)));

String statesToJson(List<States> data) => json.encode(List<dynamic>.from(data.map((x) => x.toJson())));

class States {
    States({
        this.title,
        this.code,
        this.id,
    });

    String title;
    String code;
    int id;

    factory States.fromJson(Map<String, dynamic> json) => States(
        title: json["title"],
        code: json["code"],
        id: json["id"],
    );

    Map<String, dynamic> toJson() => {
        "title": title,
        "code": code,
        "id": id,
    };
}