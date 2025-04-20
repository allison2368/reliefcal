from typing import Any
import httpx
import os
from cerebras.cloud.sdk import Cerebras
import json
import re
import asyncio

client = Cerebras(
    # This is the default and can be omitted
    api_key=os.environ.get("CEREBRAS_API_KEY"),
)

## TOOL DEF ===================================

# Constants
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

async def make_nws_request(url: str) -> dict[str, Any] | None:
    """Make a request to the NWS API with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

async def get_forecast(latitude: float, longitude: float) -> str:
    """Get weather forecast for a location.

    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
    """
    # First get the forecast grid endpoint
    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = await make_nws_request(points_url)

    if not points_data:
        return "Unable to fetch forecast data for this location."

    # Get the forecast URL from the points response
    forecast_url = points_data["properties"]["forecast"]
    forecast_data = await make_nws_request(forecast_url)

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

## ============================================

def calculate(expression):
    expression = re.sub(r'[^0-9+\-*/().]', '', expression)
    
    try:
        result = eval(expression)
        return str(result)
    except (SyntaxError, ZeroDivisionError, NameError, TypeError, OverflowError):
        return "Error: Invalid expression"

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather_forecast",
            "strict": True,
            "description": "A tool that gets current weather forecasts. Use this when the user asks for live weather data (implicitly or explicitly)",
            "parameters": {
                "type": "object",
                "properties": {
                    "longitude": {
                        "type": "number",
                        "description": "The longitude of the requested location"
                    },
                    "latitude": {
                      "type": "number",
                      "description":" The latitude of the requested location"
                    }
                },
                "required": ["longitude", "latitude"]
            }
        }
    }
]

base_messages = [
    {"role": "system", "content": "You are acting as a search engine for results, and you have many tools that can query you the data you need. When answering, please provide a quick, 1 sentence response."},
    # {"role": "user", "content": "What's the result of 15 multiplied by 7?"},
]

async def prompt():
  question = input("Ask a question!: ")
  while question != "exit":
    messages = [*base_messages, {
      "role": "user",
      "content": question
    }]
    
    response = client.chat.completions.create(
      tools=tools,
      parallel_tool_calls=False,
      messages=messages,
        model="llama-4-scout-17b-16e-instruct",
    )
    
    choice = response.choices[0].message

    if choice.tool_calls:
        function_call = choice.tool_calls[0].function
        if function_call.name == "get_weather_forecast":
            # Logging that the model is executing a function named "calculate".
            print(f"Model executing function '{function_call.name}' with arguments {function_call.arguments}")

            # Parse the arguments from JSON format and perform the requested calculation.
            arguments = json.loads(function_call.arguments)
            result = await get_forecast(latitude = arguments["latitude"], longitude = arguments["longitude"])

            # Note: This is the result of executing the model's request (the tool call), not the model's own output.
            print(f"Calculation result sent to model: {result}")
          
          # Send the result back to the model to fulfill the request.
            messages.append({
                "role": "tool",
                "content": json.dumps(result),
                "tool_call_id": choice.tool_calls[0].id
            })
    
          # Request the final response from the model, now that it has the calculation result.
            final_response = client.chat.completions.create(
                model="llama-4-scout-17b-16e-instruct",
                messages=messages,
            )
            
            # Handle and display the model's final response.
            if final_response:
                print("Final model output:", final_response.choices[0].message.content)
            else:
                print("No final response received")
    else:
        # Handle cases where the model's response does not include expected tool calls.
        print("Unexpected response from the model")
    
    print()
    question = input("Ask a question!: ") 

asyncio.run(prompt())