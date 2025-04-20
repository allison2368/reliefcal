# Constants
import json
from backend.custom_tools.tool import Tool

from backend.network import make_request_post

API_KEY = "AIzaSyAC1c_yUCOj-UpfK6ReYzDmS42HuR6Gwb8"  # Replace with your actual API key

class PoliceTool(Tool):
    def __init__(self):
        super().__init__(name="police_tool",
                         description="A tool that gets nearby police stations given a location. Use this when the user asks for police stations. It will return an with a field results, which is an array of json objects representing the police stations, where displayName is an HTML string containing the name, googleMapsUri is the URL for the police station, and adrFormatAddress is the address.",
                         properties={
							"latitude": {
								"type": "number",
								"description":" The latitude of the requested location"
							},
							"longitude": {
								"type": "number",
								"description": "The longitude of the requested location"
							}
                         })

    async def tool_call(self, latitude: float, longitude: float):
        police_stations = await make_request_post("https://places.googleapis.com/v1/places:searchText", headers={
            "X-Goog-Api-Key": API_KEY,
            "X-Goog-FieldMask": "places.displayName,places.googleMapsUri,places.adrFormatAddress"
        }, data={
            "textQuery": "police stations",
        })
        
        if police_stations:
            return json.dumps(police_stations)
        return "Something Went Wrong."
