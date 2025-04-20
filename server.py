import asyncio
from backend.search import search
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/search")
def hello_world():
    query = request.args.get('query', '')
    
    result = asyncio.run(search(query))
    
    return json.loads(result);