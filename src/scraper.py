import json
import requests

def grab_json(url_base):
    constructed_url = build_url(url_base)
    res = requests.get(constructed_url)

    if res:
        if res.status_code == 200:
            return res.content
        elif res.status_code == 404:
            raise Exception(f"No content found at {constructed_url}")
        # more response codes here
    else:
        raise Exception(f"No response from {constructed_url}.")

def build_url(base):
    return base + "/vatsim-data.json"

if __name__ == "__main__":
    print(grab_json("http://data.vatsim.net"))