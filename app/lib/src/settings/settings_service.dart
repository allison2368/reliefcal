import 'package:shared_preferences/shared_preferences.dart';

/// A service that stores and retrieves user settings.
///
/// By default, this class does not persist user settings. If you'd like to
/// persist the user settings locally, use the shared_preferences package. If
/// you'd like to store settings on a web server, use the http package.
class SettingsService {
  late SharedPreferences asyncPrefs;

  Future<String> zipCode() async => await asyncPrefs.getString("zipCode") ?? "95618";

  Future<void> updateZipCode(String zipCode) async {
    asyncPrefs.setString("zipCode", zipCode);
  }

  Future<void> init() async {
    asyncPrefs = await SharedPreferences.getInstance();
  }
}
