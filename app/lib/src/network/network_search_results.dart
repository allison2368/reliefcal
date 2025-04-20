import 'dart:convert';

import 'package:http/http.dart' as http;

class SearchResult {
  final String name;
  final String type;
  final double? latitude;
  final double? longitude;
  final String url;
  final String? description;

  const SearchResult(
      {required this.name,
      required this.type,
      this.latitude,
      this.longitude,
      required this.url,
      this.description});

  factory SearchResult.fromJson(Map<String, dynamic> json) {
    return switch (json) {
      {
        'name': String name,
        'type': String type,
        'latitude': double? latitude,
        'longitude': double? longitude,
        'url': String url,
        'description': String? description,
      } =>
        SearchResult(
          name: name,
          type: type,
          latitude: latitude,
          longitude: longitude,
          url: url,
          description: description,
        ),
      _ => throw const FormatException('Failed to load SearchResult.'),
    };
  }
}

Future<List<SearchResult>> fetchResults({query = String}) async {
  print("fetching results with query $query");
  final response = await http.get(
    Uri.parse(
        'http://18.117.104.11:5000/search?query=${query.toString().replaceAll(" ", "%20")}'),
  );

  if (response.statusCode == 200) {
    // If the server did return a 200 OK response,
    // then parse the JSON.

    // Parse the JSON string into a Dart Map
    print(response.body);
    Map<String, dynamic> jsonData = jsonDecode(response.body);

    bool? success = jsonData['success'];

    if (success != null && success) {
      print("got results");
      // Access the 'results' list
      List<dynamic> results = jsonData['results'];

      print(results);

      return results.map((result) => SearchResult.fromJson(result)).toList();
    } else {
      throw Exception(jsonData['reason']);
    }
  } else {
    // If the server did not return a 200 OK response,
    // then throw an exception.
    throw Exception('Failed to load search result');
  }
}
