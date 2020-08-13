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
        this.charges,
    });

    DateTime dateBillPrepared;
    String tierWaterUsage;
    String serviceChargeTotal;
    String totalAmount;
    DateTime dueDate;
    int id;
    List<String> charges;

    factory Bill.fromJson(Map<String, dynamic> json) => Bill(
        dateBillPrepared: DateTime.parse(json["date_bill_prepared"]),
        tierWaterUsage: json["tier_water_usage"],
        serviceChargeTotal: json["service_charge_total"],
        totalAmount: json["total_amount"],
        dueDate: DateTime.parse(json["due_date"]),
        id: json["id"],
        charges: List<String>.from(json["charges"].map((x) => x)),
    );

    Map<String, dynamic> toJson() => {
        "date_bill_prepared": dateBillPrepared.toIso8601String(),
        "tier_water_usage": tierWaterUsage,
        "service_charge_total": serviceChargeTotal,
        "total_amount": totalAmount,
        "due_date": dueDate.toIso8601String(),
        "id": id,
        "charges": List<dynamic>.from(charges.map((x) => x)),
    };
}