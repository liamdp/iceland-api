import requests
import json

def put(url, payload):
    try:
        request = requests.put(url,
                    data = json.dumps(payload),
                    headers={"content-type":"application/json"}
                    )
        if request.ok:
            print("Success!")
        else:
            print("Something went wrong when making put request but a connection was established.")
    except:
        print("Could not establish connection or something went wrong making the request.")
