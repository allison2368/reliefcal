from abc import abstractmethod

class Tool:
  def __init__(self,
               name: str="",
               description: str="",
               properties:dict[str, dict]=""):
    self.name = name
    self.description = description
    self.properties = properties
    pass
  
  @abstractmethod
  async def tool_call(self) -> str:
      pass
    
  def toCerebrasTool(self):
    return {
      "type": "function",
      "function": {
        "name": self.name,
        "strict": True,
        "description": self.description,
        "parameters": {
          "type": "object",
          "properties": self.properties,
        },
        "required": list(self.properties.keys())
      }
    }