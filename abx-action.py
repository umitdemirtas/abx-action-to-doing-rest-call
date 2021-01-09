"""
Inputs:
   - endpoint: <your-rest-endpoint>

Dependency:
    - requests
"""

def handler(context, inputs):
    import requests
    import json
    import datetime as date
    
    data = {
        "inputs": inputs
    }
    
    now = date.datetime.now()
    shortDate = now.strftime("%Y-%m-%d")
    shortTime = now.strftime("%H:%M:%S")

    payload = {
        "id": inputs["id"],
        "date": shortDate + " " + shortTime,
        "data": data
    }
    
    baseURL = inputs["endpoint"]
    headers = {
        "Authorization": "Bearer XXxXX"
    }

    payload = json.dumps(payload)
    
    response = requests.post(baseURL, data=payload, headers=headers)
    print("Status Code " + str(response.status_code))
    
    return str(response.status_code)
