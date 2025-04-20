import json
from typing import Any
from backend.custom_tools.hospitals import HospitalTool
from backend.custom_tools.tool import Tool
from backend.custom_tools.weather import WeatherTool
from backend.custom_tools.women import WomenResourceTool
from backend.custom_tools.fire import FireTool
from backend.custom_tools.police import PoliceTool
from backend.custom_tools.food import FoodTool
from backend.custom_tools.salvationarmy import SalvationTool
from backend.custom_tools.redcross import RedCrossTool
class Tools:
  tools: dict[str, Tool] = {}
  
  def registerTool(self, tool: Tool):
    self.tools[tool.name] = tool
    
  async def callTools(self, choice: Any):
    # choice = response.choices[0].message

    # if choice.tool_calls:
    messages = []
    
    if choice.message.tool_calls:
      for tool_call in choice.message.tool_calls:
        function_call = tool_call.function
        tool = self.tools[function_call.name]
        
        if tool is None:
          continue
        
        print(f"Model executing function '{function_call.name}' with arguments {function_call.arguments}")
        
        arguments = json.loads(function_call.arguments)
        result = await tool.tool_call(**arguments)
        
        print("Tool call finished.")
        
        # Send the result back to the model to fulfill the request.
        messages.append({
            "role": "tool",
            "content": json.dumps(result),
            "tool_call_id": tool_call.id
        })
    else:
        # Handle cases where the model's response does not include expected tool calls.
        print("Unexpected response from the model")
        
    return messages
  
  def toCerebrasTools(self):
    return [tool.toCerebrasTool() for tool in self.tools.values()]
  
all_tools = Tools()

# add your tools here!
all_tools.registerTool(WeatherTool())
all_tools.registerTool(HospitalTool())
all_tools.registerTool(WomenResourceTool())
all_tools.registerTool(FireTool())
all_tools.registerTool(PoliceTool())
all_tools.registerTool(FoodTool())
all_tools.registerTool(SalvationTool())
all_tools.registerTool(RedCrossTool())