import json
import requests

def grab_json(url):
    res = requests.get(url)

    if res:
        if res.status_code == 200:
            return res.content
        elif res.status_code == 404:
            raise Exception(f"No content found at {url}")
        # more response codes here
    else:
        raise Exception(f"No response from {url}.")

if __name__ == "__main__":
    print(grab_json("http://data.vatsim.net"))