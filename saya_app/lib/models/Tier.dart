// To parse this JSON data, do
//
//     final tier = tierFromJson(jsonString);

import 'dart:convert';

List<Tier> tierFromJson(String str) => List<Tier>.from(json.decode(str).map((x) => Tier.fromJson(x)));

String tierToJson(List<Tier> data) => json.encode(List<dynamic>.from(data.map((x) => x.toJson())));

class Tier {
    Tier({
        this.title,
        this.tierRangeLow,
        this.tierRangeHigh,
    });

    String title;
    int tierRangeLow;
    int tierRangeHigh;

    factory Tier.fromJson(Map<String, dynamic> json) => Tier(
        title: json["title"],
        tierRangeLow: json["tier_range_low"],
        tierRangeHigh: json["tier_range_high"],
    );

    Map<String, dynamic> toJson() => {
        "title": title,
        "tier_range_low": tierRangeLow,
        "tier_range_high": tierRangeHigh,
    };
}
