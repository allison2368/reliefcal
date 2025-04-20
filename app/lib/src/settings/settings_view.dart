import 'package:flutter/material.dart';

import 'settings_controller.dart';

class SettingsView extends StatefulWidget {
  static const routeName = '/settings';

  const SettingsView({super.key, required this.controller});
  
  final SettingsController controller;

  @override
  State<StatefulWidget> createState() => _SettingsViewState();

}

/// Displays the various settings that can be customized by the user.
///
/// When a user changes a setting, the SettingsController is updated and
/// Widgets that listen to the SettingsController are rebuilt.
class _SettingsViewState extends State<SettingsView> {

  late TextEditingController _textController;

  @override
  void initState() {
      super.initState();

      _textController = TextEditingController(
        text: widget.controller.zipCode
      );
      
      _textController.addListener(() {
        widget.controller.updateZipCode(_textController.text);
      });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Settings'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        // Glue the SettingsController to the theme selection DropdownButton.
        //
        // When a user selects a theme from the dropdown list, the
        // SettingsController is updated, which rebuilds the MaterialApp.
        child: TextField(
          // Read the selected themeMode from the controller
          // Call the updateThemeMode method any time the user selects a theme.
          controller: _textController,
        ),
      ),
    );
  }
}
