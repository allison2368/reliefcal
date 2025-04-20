import json
import os
from cerebras.cloud.sdk import Cerebras
from backend.tools import all_tools

client = Cerebras(
    # This is the default and can be omitted
    api_key=os.environ.get("CEREBRAS_API_KEY"),
)

tools = all_tools.toCerebrasTools()

# context_prompt = """
# You are acting as a search engine for emergency/public/private services in the area, and you have many tools that can query you the data you need.

# When answering, please provide the response as a list of json objects with the following desirable fields:

# 'name',
# 'url',
# 'latitude' (if not applicable, set to null),
# 'longitude' (if not applicable, set to null),
# 'type',
# 'description',
# 'additional' which is an object that can contain any seemingly relevant information.

# The field 'type' can be something like, 'hosptial', 'weather', 'event', etc.

# You can infer what each of these fields should mean, just keep it consistent.
# You may call multiple tools and aggregate the data together all into one big array.
# It's okay to have multiple types in the array.
# If there is not enough sufficient data, this is a failure, and the reason is not enough data.
# Do not try to make new data, only use the data directly provided.
# If there are duplicants in the data, please remove them, and choose what seems best.
# Respond with only JSON, no additional text whatsoever. No backquotes.

# All successful responses are in the form
# {
#     success: true,
#     results: insert_array_here,
# }

# where results is the array of all of the results that you got from before.

# and all responses with failures are in the form
# {
#     success: false,
#     reason: string,
# }

# Triple backquotes (```) are invalid JSON.

# Please conform to these and be exact. Do not output backquotes, that is not valid JSON. You will always output valid JSON.
# """
context_prompt = """
You are acting as a search engine for results, and you have many tools that can query you the data you need.

When answering, please provide the response as a list of json objects with the following desirable fields:

'name',
'url',
'latitude' (if not applicable, set to null),
'longitude' (if not applicable, set to null),
'type',
'description',
'additional' which is an object that can contain any seemingly relevant information.

The field 'type' can be something like, 'hospital', 'weather', 'event', etc.

You can infer what each of these fields should mean, just keep it consistent.
If you have data of multiple types, put them all in the same array.
If there is not enough sufficient data, please say 'Not Enough Data'.
Do not try to make new data, only use the data directly provided and be exact.
If there are duplicants in the data, please remove them, and choose what seems best.
Do not include additional text, only the JSON object.
Be exact with the data.

All successful responses are in the form
{
    success: true,
    results: T[],
}

and all responses with failures are in the form
{
    success: false,
    reason: string,
}

Please conform to these. You will always output valid JSON. When in doubt, output the failure form.
"""

base_messages = [
    {"role": "system", "content": context_prompt},
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
        response_format={"type": "json_object"}
    )

    # Handle and display the model's final response.
    if final_response:
        return final_response.choices[0].message.content
    else:
        return None