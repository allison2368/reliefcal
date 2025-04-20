import 'package:flutter/material.dart';
import 'package:team_moo_moo/src/network/network_search_results.dart';

class SearchResultWidget extends StatelessWidget {
  const SearchResultWidget({super.key, required this.result});

  final SearchResult result;

  @override
  Widget build(BuildContext context) {
    return Card.outlined(
        child: Padding(
      padding: const EdgeInsets.all(12.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            result.name,
            style: const TextStyle(
              fontSize: 20,
              fontWeight: FontWeight.w600,
            ),
          ),
          result.description != null
              ? Text(result.description!)
              : const SizedBox.shrink(),
          const SizedBox(height: 8),
          Row(
            mainAxisAlignment: MainAxisAlignment.end,
            children: [
              OutlinedButton.icon(
                  onPressed: () {
                    print("attempting to launch ${result.url}");
                  },
                  icon: const Icon(Icons.language),
                  label: const Text("Website")),
              const SizedBox(width: 8),
              OutlinedButton.icon(
                  onPressed: () {},
                  icon: const Icon(Icons.directions),
                  label: const Text("Directions"))
            ],
          )
        ],
      ),
    ));
  }
}
