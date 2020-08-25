// To parse this JSON data, do
//
//     final notifications = notificationsFromJson(jsonString);

import 'dart:convert';

List<Notifications> notificationsFromJson(String str) => List<Notifications>.from(json.decode(str).map((x) => Notifications.fromJson(x)));

String notificationsToJson(List<Notifications> data) => json.encode(List<dynamic>.from(data.map((x) => x.toJson())));

class Notifications {
    Notifications({
        this.title,
        this.subtitle,
        this.datePosted,
        this.id,
    });

    String title;
    String subtitle;
    DateTime datePosted;
    int id;

    factory Notifications.fromJson(Map<String, dynamic> json) => Notifications(
        title: json["title"],
        subtitle: json["subtitle"],
        datePosted: DateTime.parse(json["date_posted"]),
        id: json["id"],
    );

    Map<String, dynamic> toJson() => {
        "title": title,
        "subtitle": subtitle,
        "date_posted": datePosted.toIso8601String(),
        "id": id,
    };
}
