import json
from pathlib import Path
import pandas as pd
from backend.custom_tools.tool import Tool

women_df = pd.read_csv(Path("data/women.csv").resolve(), encoding="ISO-8859-1")
women_df.columns = women_df.columns.str.replace(" ", "")
women_df["VENDOR"].str.strip()
class WomenResourceTool(Tool):
  def __init__(self):
      super().__init__(name="women_tool",
                       description="A tool that gets nearby women resource given a location. Use this when the user asks for nearby facilities that redeem vouchers with WIC food instruments and vouchers.. It will return a json array with the vendor's 'VENDOR', 'ADDRESS', 'LATITUDE', and 'LONGITUDE'.",
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
    filtered_df = women_df[
      (women_df['LONGITUDE'] >= longitude - 0.1) & (women_df['LONGITUDE'] <= longitude + 0.1) &
      (women_df['LATITUDE'] >= latitude - 0.1) & (women_df['LATITUDE'] <= latitude + 0.1)
    ][["VENDOR", "ADDRESS", "LONGITUDE", "LATITUDE"]][:10]
    

    
    return filtered_df.to_json()
  
  pass