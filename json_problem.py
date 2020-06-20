import requests
import json

response = requests.get("http://httpbin.org/get")
dict1 = json.loads(response.text)

print(dict1['origin'])
