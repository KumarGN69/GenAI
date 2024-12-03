# importing requests for API calls and json for formating
import requests
import os
from dotenv import load_dotenv
from pprint import pprint
load_dotenv()

API_ENDPOINT = os.getenv("TAVILY_SEARCH_API_ENDPOINT")
API_KEY = os.getenv("TAVILY_API_KEY")
print(API_KEY)
print(API_ENDPOINT)

# QUERY = input("What do you want to search?: ")
QUERY = "What is the best way to read pdf files in GenAI?"
def tavily_search(query):
    """ search function using Tavily API"""
    headers = {
        "Content-Type": "application/json"
    }

    query_payload = {
    "api_key": API_KEY,
    "query": query,
    }

    params= {
    "search_depth": "basic",
    "max_results": 10
    }

    response = requests.post(API_ENDPOINT, json=query_payload, params=params, timeout=15, verify=True)
    response.raise_for_status()

    if response.status_code == 200:
        return response.json()
    else:
        print("error encountered")
        return f"Error: {response.status_code}. {response.text}"


results = tavily_search(query=QUERY)
pprint(results)
