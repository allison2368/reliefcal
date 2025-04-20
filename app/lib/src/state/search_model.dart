import 'package:flutter/foundation.dart';

class SearchModel with ChangeNotifier, DiagnosticableTreeMixin {
  String _query = "";

  String get query => _query;

  void changeQuery(String query) {
    _query = query;

    notifyListeners();
  }

  /// Makes `SearchModel` readable inside the devtools by listing all of its properties
  @override
  void debugFillProperties(DiagnosticPropertiesBuilder properties) {
    super.debugFillProperties(properties);
    properties.add(StringProperty('query', query));
  }
}