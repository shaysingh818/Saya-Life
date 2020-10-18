// To parse this JSON data, do
//
//     final bill = billFromJson(jsonString);

import 'dart:convert';

List<Bill> billFromJson(String str) => List<Bill>.from(json.decode(str).map((x) => Bill.fromJson(x)));

String billToJson(List<Bill> data) => json.encode(List<dynamic>.from(data.map((x) => x.toJson())));

class Bill {
    Bill({
        this.dateBillPrepared,
        this.tierWaterUsage,
        this.serviceChargeTotal,
        this.totalAmount,
        this.dueDate,
        this.id,
    });

    DateTime dateBillPrepared;
    TierWaterUsage tierWaterUsage;
    String serviceChargeTotal;
    String totalAmount;
    DateTime dueDate;
    int id;

    factory Bill.fromJson(Map<String, dynamic> json) => Bill(
        dateBillPrepared: DateTime.parse(json["date_bill_prepared"]),
        tierWaterUsage: tierWaterUsageValues.map[json["tier_water_usage"]],
        serviceChargeTotal: json["service_charge_total"],
        totalAmount: json["total_amount"],
        dueDate: DateTime.parse(json["due_date"]),
        id: json["id"],
    );

    Map<String, dynamic> toJson() => {
        "date_bill_prepared": dateBillPrepared.toIso8601String(),
        "tier_water_usage": tierWaterUsageValues.reverse[tierWaterUsage],
        "service_charge_total": serviceChargeTotal,
        "total_amount": totalAmount,
        "due_date": dueDate.toIso8601String(),
        "id": id,
    };
}

enum TierWaterUsage { TIER_3_LA_UNDER_10999, TIER_4_LA_UNDER_10999 }

final tierWaterUsageValues = EnumValues({
    "Tier 3 : LA_Under_10999": TierWaterUsage.TIER_3_LA_UNDER_10999,
    "Tier 4 : LA_Under_10999": TierWaterUsage.TIER_4_LA_UNDER_10999
});

class EnumValues<T> {
    Map<String, T> map;
    Map<T, String> reverseMap;

    EnumValues(this.map);

    Map<T, String> get reverse {
        if (reverseMap == null) {
            reverseMap = map.map((k, v) => new MapEntry(v, k));
        }
        return reverseMap;
    }
}
