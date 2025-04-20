# Constants
import json
from backend.custom_tools.tool import Tool
import googlemaps

from backend.network import make_request_post

API_KEY = "AIzaSyAC1c_yUCOj-UpfK6ReYzDmS42HuR6Gwb8"  # Replace with your actual API key

class FoodTool(Tool):
    def __init__(self):
        super().__init__(name="food_tool",
                         description="A tool that looks for nearby food co-op or free food distribution centers or food banks given a location. Use this when the user asks for food banks. It will return an with a field results, which is an array of json objects representing the food bank informations, where displayName is an HTML string containing the name, googleMapsUri is the URL for the food bank, and adrFormatAddress is the address",
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
        food_banks = await make_request_post("https://places.googleapis.com/v1/places:searchText", headers={
            "X-Goog-Api-Key": API_KEY,
            "X-Goog-FieldMask": "places.displayName,places.googleMapsUri,places.adrFormatAddress"
        }, data={
            "textQuery": "food banks",
        })

        print(food_banks)
        # fire_stations = gmaps.places(query=query, location={
        #     "lat": latitude,
        #     "lng": longitude
        #     }, radius=5000)
        # 
        # print(fire_stations)
        # fire_stations = await nearby_text_search(latitude, longitude, 5000, query)
        
        if food_banks:
            return json.dumps(food_banks)
        return "Something Went Wrong."
