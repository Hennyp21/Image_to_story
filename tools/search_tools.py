import os
import requests
import json 
from langchain.tools import tool
class SerperSearchTool():
    @tool("search")
    def search(query: str) -> str:
        """Useful to search the internet about a given topic and return relevant
    results."""
        url = "https://google.serper.dev/search"
        headers = {
            "X-API-KEY": os.getenv("SERPER_API_KEY"),
            "Content-Type": "application/json"
        }
        data = {"q": query}
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()

        snippets = []
        for item in result.get("organic", [])[:3]:
            snippet = item.get("snippet")
            if snippet:
                snippets.append(f"- {snippet}")

        return "\n".join(snippets) if snippets else "No relevant search results found."