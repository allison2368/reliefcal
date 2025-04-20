import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:team_moo_moo/src/components/PremadeOptions.dart';
import 'package:team_moo_moo/src/components/option.dart';
import 'package:team_moo_moo/src/components/search_results.dart';
import 'package:team_moo_moo/src/state/search_model.dart';

import '../components/my_search_bar.dart';
import '../sample_feature/sample_item.dart';
import '../settings/settings_view.dart';

class HomePage extends StatelessWidget {
  const HomePage({
    super.key,
    this.items = const [SampleItem(1), SampleItem(2), SampleItem(3)],
  });

  static const routeName = '/';

  final List<SampleItem> items;

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (_) => SearchModel(),
      child: Scaffold(
          appBar: AppBar(
            title: const Text('Sample Items'),
            actions: [
              IconButton(
                icon: const Icon(Icons.settings),
                onPressed: () {
                  // Navigate to the settings page. If the user leaves and returns
                  // to the app after it has been killed while running in the
                  // background, the navigation stack is restored.
                  Navigator.restorablePushNamed(
                      context, SettingsView.routeName);
                },
              ),
            ],
          ),

          // To work with lists that may contain a large number of items, it’s best
          // to use the ListView.builder constructor.
          //
          // In contrast to the default ListView constructor, which requires
          // building all Widgets up front, the ListView.builder constructor lazily
          // builds Widgets as they’re scrolled into view.
          body: const Padding(
            padding: EdgeInsets.fromLTRB(16, 0, 16, 16),
            child: Column(children: [
              MySearchBar(title: "Search"),
              PremadeOptions(title: "Emergency", children: [
                Option(emoji: "🔥", text: "Fire"),
                Option(emoji: "🏥", text: "Hospitals"),
                Option(emoji: "👮", text: "Police"),
              ]),
              PremadeOptions(title: "Non-Emergency", children: [
                Option(emoji: "♀️", text: "Womens' Health Care"),
                Option(emoji: "☀️", text: "Weather"),
              ]),
              SearchResults()
            ]),
          )),
    );
  }
}
