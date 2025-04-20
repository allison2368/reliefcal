import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:team_moo_moo/src/components/search_result.dart';
import 'package:team_moo_moo/src/network/network_search_results.dart';
import 'package:team_moo_moo/src/settings/settings_controller.dart';
import 'package:team_moo_moo/src/state/search_model.dart';

class SearchResultsConsumer extends StatelessWidget {
  const SearchResultsConsumer({super.key, required this.controller});

  final SettingsController controller;

  @override
  Widget build(BuildContext context) {
    return SearchResults(query: "${context.watch<SearchModel>().query} in ${controller.zipCode}");
  }
}

class SearchResults extends StatefulWidget {
  const SearchResults({super.key, required this.query});

  final String query;

  @override
  State<StatefulWidget> createState() => _SearchResults();
}

class _SearchResults extends State<SearchResults> {
  List<SearchResult> searchResults = [];
  String? errorReason;

  @override
  void didUpdateWidget(covariant SearchResults oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (widget.query != oldWidget.query) {
      // Only fetch data if the query parameter has changed
      fetchResults(query: widget.query).then((value) {
        setState(() {
          searchResults = value;
          errorReason = null;
        });
      }).catchError((error) {
        setState(() {
          errorReason = error.toString();
        });
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        errorReason != null
            ? Text(errorReason ?? "Error")
            : const SizedBox.shrink(),
        Expanded(
          child: ListView.builder(
            // Let the ListView know how many items it needs to build.
            itemCount: searchResults.length,
            // Provide a builder function. This is where the magic happens.
            // Convert each item into a widget based on the type of item it is.
            itemBuilder: (context, index) {
              final result = searchResults[index];
          
              return SearchResultWidget(result: result);
            },
          ),
        ),
      ],
    );
  }
}
