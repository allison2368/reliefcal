import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:team_moo_moo/src/state/search_model.dart';

class MySearchBar extends StatefulWidget {
  final String title;
  

  const MySearchBar({super.key, required this.title, });

  @override
  State<MySearchBar> createState() => _MySearchBarState();
}

class _MySearchBarState extends State<MySearchBar> {
  final TextEditingController _controller = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Expanded(
          child: TextField(
            controller: _controller,
            decoration: InputDecoration(
              contentPadding: const EdgeInsets.fromLTRB(16.0, 6, 16.0, 6.0),
              hintText: "What do you need help with?",
              border: OutlineInputBorder(
                borderRadius: BorderRadius.circular(
                    25.0), // Adjust the radius for desired roundness
                borderSide: BorderSide(
                  color:
                      Colors.grey.shade400, // Choose your desired border color
                  width:
                      1.0, // Adjust the width for a thinner or thicker border
                ),
              ),
              enabledBorder: OutlineInputBorder(
                borderRadius: BorderRadius.circular(25.0),
                borderSide: BorderSide(
                  color: Colors.grey.shade400,
                  width: 1.0,
                ),
              ),
              focusedBorder: OutlineInputBorder(
                borderRadius: BorderRadius.circular(25.0),
                borderSide: const BorderSide(
                  color: Colors.blue, // Color when the TextField is focused
                  width: 1.0,
                ),
              ),
            ),
          ),
        ),
        const SizedBox(width: 16.0),
        IconButton(
          icon: const Icon(
            Icons.search,
            color: Colors.white, // Set the icon color here
          ), // Replace with your desired icon
          onPressed: () {
            // Add your onPressed logic here
            print("Searching for ${_controller.text}");
            context.read<SearchModel>().changeQuery(_controller.text);
          },
          style: ButtonStyle(
            backgroundColor:
                WidgetStateProperty.all<Color>(Theme.of(context).primaryColor),
            shape: WidgetStateProperty.all<CircleBorder>(
              const CircleBorder(),
            ),
            padding: WidgetStateProperty.all<EdgeInsetsGeometry>(
                const EdgeInsets.all(12.0)), // Adjust padding as needed
          ),
        )
      ],
    );
  }
}
