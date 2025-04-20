import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:team_moo_moo/src/state/search_model.dart';

class SearchResults extends StatefulWidget {
  const SearchResults({super.key});

  @override
  State<StatefulWidget> createState() => _SearchResults();
}

class _SearchResults extends State<SearchResults> {
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        const Text("hi"),
        Text(context.watch<SearchModel>().query),
      ],
    );
  }
}
