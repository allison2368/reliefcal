import 'package:flutter/material.dart';

class Option extends StatelessWidget {
  final String emoji;
  final String text;
  final VoidCallback? onTap; // Make onTap optional

  const Option({
    super.key, // Use Key?
    required this.emoji,
    required this.text,
    this.onTap, // Make onTap optional
  });

  @override
  Widget build(BuildContext context) {
    return OutlinedButton(
      onPressed: () {},
      style: ButtonStyle(
          padding: WidgetStateProperty.all<EdgeInsetsGeometry>(
              const EdgeInsets.symmetric(horizontal: 12.0, vertical: 4.0))),
      child: Row(
        children: [
          Text(
            emoji,
            style: const TextStyle(fontSize: 16.0), // Adjust size as needed
          ),
          const SizedBox(width: 4.0), // Space between emoji and text
          Text(
            text,
            style: const TextStyle(fontSize: 14.0), // Adjust text style
          ),
        ],
      ),
    );
  }
}
