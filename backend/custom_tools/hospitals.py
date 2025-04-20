import json
from pathlib import Path
import pandas as pd
from backend.custom_tools.tool import Tool

hospital_df = pd.read_csv(Path("data/hospitals.csv").resolve(), encoding="ISO-8859-1")

class HospitalTool(Tool):
  def __init__(self):
      super().__init__(name="hospital_tool",
                       description="A tool that gets nearby hospitals given a location. Use this when the user asks for hospitals",
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
    filtered_df = hospital_df[
    (hospital_df['Longitude'] >= longitude - 0.1) & (hospital_df['Longitude'] <= longitude + 0.1) &
    (hospital_df['Latitude'] >= latitude - 0.1) & (hospital_df['Latitude'] <= latitude + 0.1)
]
    print(filtered_df.to_json())
    return filtered_df.to_json()
  
  pass