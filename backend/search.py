import json
import os
from cerebras.cloud.sdk import Cerebras
from backend.tools import all_tools

client = Cerebras(
    # This is the default and can be omitted
    api_key=os.environ.get("CEREBRAS_API_KEY"),
)

tools = all_tools.toCerebrasTools()

# tools = [
#     {
#         "type": "function",
#         "function": {
#             "name": "get_weather_forecast",
#             "strict": True,
#             "description": "A tool that gets current weather forecasts. Use this when the user asks for live weather data (implicitly or explicitly)",
#             "parameters": {
#                 "type": "object",
#                 "properties": {
#                     "longitude": {
#                         "type": "number",
#                         "description": "The longitude of the requested location"
#                     },
#                     "latitude": {
#                       "type": "number",
#                       "description":" The latitude of the requested location"
#                     }
#                 },
#                 "required": ["longitude", "latitude"]
#             }
#         }
#     }
# ]


test = [
    {
        'type': 'function',
        'function': {
            'name': 'weather_tool',
            'strict': True,
            'description':'A tool that gets current weather forecasts. Use this when the user asks for live weather data (implicitly or explicitly)',
            'properties': {
                'longitude': {
                    'type': 'number', 
                    'description': 'The longitude of the requested location'
                },
                'latitude': {
                    'type': 'number',
                    'description': ' The latitude of the requested location'
                }
            },
            'required': ['longitude', 'latitude']
            }
        }
    ]

base_messages = [
    {"role": "system", "content": "You are acting as a search engine for results, and you have many tools that can query you the data you need. When answering, please provide a quick, 1 sentence response."},
    # {"role": "user", "content": "What's the result of 15 multiplied by 7?"},
]

async def search(question: str) -> str:
    
    messages = [*base_messages, {
        "role": "user",
        "content": question
    }]
    
    initial_response = client.chat.completions.create(
        tools=tools,
        parallel_tool_calls=False,
        messages=messages,
        model="llama-4-scout-17b-16e-instruct",
    )
    
    newMessages = await all_tools.callTools(initial_response.choices[0])
    messages = messages + newMessages
    
    # Request the final response from the model, now that it has the calculation result.
    final_response = client.chat.completions.create(
        messages=messages,
        model="llama-4-scout-17b-16e-instruct",
    )

    # Handle and display the model's final response.
    if final_response:
        return final_response.choices[0].message.content
    else:
        return None