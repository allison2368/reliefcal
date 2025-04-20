import 'package:flutter/material.dart';

class PremadeOptions extends StatelessWidget {
  const PremadeOptions({Key? key, this.title = "NO TITLE", this.children = const []}) : super(key: key);

  final String title;
  final List<Widget> children;

  @override
  Widget build(BuildContext context) {
    List<Widget> spacedChildren = [];

    for (Widget child in children) {
      spacedChildren.add(child);
      spacedChildren.add(SizedBox(width: 8.0));
    }

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        const SizedBox(height: 16.0),
        Text(title, style: const TextStyle(fontWeight: FontWeight.bold)),
        const SizedBox(height: 4.0),
        Row(
          children: spacedChildren,
        )
      ],
    ); // Or any other empty widget
  }
}
