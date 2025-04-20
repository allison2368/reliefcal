import 'package:flutter/material.dart';

class PremadeOptions extends StatelessWidget {
  const PremadeOptions({Key? key, this.title = "NO TITLE", this.children = const []}) : super(key: key);

  final String title;
  final List<Widget> children;

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        const SizedBox(height: 16.0),
        Text(title, style: const TextStyle(fontWeight: FontWeight.bold)),
        const SizedBox(height: 4.0),
        Wrap(
          spacing: 8.0, // gap between adjacent chips
          runSpacing: 4.0, // gap between lines
          children: children,
        )
      ],
    ); // Or any other empty widget
  }
}
