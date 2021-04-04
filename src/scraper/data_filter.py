import json

def import_json(scraped_json):
    json_file = json.loads(scraped_json)
    return json_file
    
def filter_atc(json_file):
    if json_file == '' or json_file == None:
        raise Exception("JSON file not imported. Make sure 'import_json' was run first.")

    clients = json_file["clients"]
    atc_clients = []

    for client in clients:
        if client["clienttype"] == "ATC" and "atis" not in client["callsign"].lower():
            atc_clients.append(client)

    return atc_clients

def filter_iceland_pos(atc_clients, filter_positions):
    filtered_stations = {}
    filtered_stations["atc"] = []
    for atc_client in atc_clients:
        for position in filter_positions:
            if position in atc_client["callsign"]:
                filtered_stations["atc"].append({
                    "callsign" : atc_client["callsign"],
                    #"name" : atc_client["realname"], # possible GDPR nonsense
                    "cid" : atc_client["cid"],
                    "frequency": atc_client["frequency"],
                })
    
    return filtered_stations
