// To parse this JSON data, do
//
//     final lotSize = lotSizeFromJson(jsonString);

import 'dart:convert';

List<LotSize> lotSizeFromJson(String str) => List<LotSize>.from(json.decode(str).map((x) => LotSize.fromJson(x)));

String lotSizeToJson(List<LotSize> data) => json.encode(List<dynamic>.from(data.map((x) => x.toJson())));

class LotSize {
    LotSize({
        this.title,
        this.lotSizeLow,
        this.lotSizeHigh,
        this.id,
    });

    String title;
    int lotSizeLow;
    int lotSizeHigh;
    int id;

    factory LotSize.fromJson(Map<String, dynamic> json) => LotSize(
        title: json["title"],
        lotSizeLow: json["lot_size_low"],
        lotSizeHigh: json["lot_size_high"],
        id: json["id"],
    );

    Map<String, dynamic> toJson() => {
        "title": title,
        "lot_size_low": lotSizeLow,
        "lot_size_high": lotSizeHigh,
        "id": id,
    };
}