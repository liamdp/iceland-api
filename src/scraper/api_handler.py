import requests
import json

def put(url, payload):
    request = requests.put(url,
                data = json.dumps(payload),
                headers={"content-type":"application/json"}
                )
    if request.ok:
        print("Success!")
    else:
        print("Something went wrong when making put request to API.")