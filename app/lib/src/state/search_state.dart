import 'package:flutter/material.dart';

class SearchState extends InheritedWidget {
  const SearchState({
    super.key,
    required this.query,
    required super.child,
  });

  final String query;

  static SearchState of(BuildContext context) {
    // This method looks for the nearest `MyState` widget ancestor.
    final result = context.dependOnInheritedWidgetOfExactType<SearchState>();

    assert(result != null, 'No SearchStateS found in context');

    return result!;
  }

  @override
  bool updateShouldNotify(SearchState oldWidget) {
    return query != oldWidget.query;
  }
}