# importing requests for API calls and json for formating
import requests
import json
import os

API_ENDPOINT = "https://api.tavily.com/search"
API_KEY = os.environ.get("TAVILY_API_KEY")
print(API_KEY)

# QUERY = input("What do you want to search?: ")
QUERY = "What is the best way to read pdf files in GenAI?"
def tavily_search(query,search_depth):
    """ search function using Tavily API"""
    auth_headers = {
    "api_key": API_KEY
    }

    query_payload = {
    "api_key": API_KEY,
    "query": query,
    "search_depth": search_depth
    }

    response = requests.post(API_ENDPOINT, headers=auth_headers, json=query_payload, timeout=15, verify=True)
    # response = {
    #     "status_code": 200,
    #     "text": "OK",
    #     "content":{
    #         "details": "Overall, Tavily aims to streamline the research process by leveraging the power of AI, enabling users to save time and make more informed decisions.\n Tavily claims to be proficient in conducting research across various subjects and niches, ranging from identifying top restaurants in a city to conducting academic research on complex topics like the economic impact of Covid. Alternative tools\nAskpot\nBiblioBot\nSpyper\nYour one-stop shop for all things AI\nPrivacy Policy\nTerms of Use\nFollow us on: The accuracy of the information provided is ensured by advanced algorithms and a team of experts who review the gathered data. The platform then gathers information from relevant sources and delivers actionable insights directly to the user\u2019s inbox in a matter of minutes."
    #         },
    #     "err_text": "Dummy error msg"
    # }
    if response.status_code == 200:
    # if response['status_code'] ==  200:
        return response.json()
        # return response['content']
    else:
        return f"Error: {response.status_code}. {response.text}"
        # return f"Error: {response['status_code']}. {response['err_text']}"

results = tavily_search(query=QUERY,search_depth="basic")
# print(results)
print(results['results'][0]['content'])
# print(results['details'])
