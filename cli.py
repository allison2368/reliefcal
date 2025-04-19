import asyncio
from pathlib import Path
import sys

from backend.search import search

sys.path.insert(0, Path.cwd())

async def prompt():
  question = input("Ask a question!: ")
  while question != "exit":
    result = await search(question)
    
    if result is not None:
      print(result)
    else:
      print("Got No Result From Model")
    
    question = input("Ask a question!: ")

asyncio.run(prompt())