# Constants
from backend.custom_tools.tool import Tool
from backend.network import make_request

NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

class WeatherTool(Tool):
  def __init__(self):
      super().__init__(name="weather_tool",
                       description="A tool that gets current weather forecasts. Use this when the user asks for live weather data (implicitly or explicitly)",
                       properties={
                          "longitude": {
                            "type": "number",
                            "description": "The longitude of the requested location"
                          },
                          "latitude": {
                            "type": "number",
                            "description":" The latitude of the requested location"
                          }
                       })
  
  async def tool_call(self, latitude: float, longitude: float):
    """Get weather forecast for a location.

    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
    """
    # First get the forecast grid endpoint
    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = await make_request(points_url)

    if not points_data:
        return "Unable to fetch forecast data for this location."

    # Get the forecast URL from the points response
    forecast_url = points_data["properties"]["forecast"]
    forecast_data = await make_request(forecast_url)

    if not forecast_data:
        return "Unable to fetch detailed forecast."

    # Format the periods into a readable forecast
    periods = forecast_data["properties"]["periods"]
    forecasts = []
    for period in periods[:5]:  # Only show next 5 periods
        forecast = f"""
{period['name']}:
Temperature: {period['temperature']}°{period['temperatureUnit']}
Wind: {period['windSpeed']} {period['windDirection']}
Forecast: {period['detailedForecast']}
"""
        forecasts.append(forecast)

    return "\n---\n".join(forecasts)

  pass