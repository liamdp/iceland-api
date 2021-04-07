import scraper
import data_filter
import file_manager
import api_handler
import random

# Vars
version = "1.0.0"
vatsim_status_url = "http://status.vatsim.net/status.json"
filter_positions = ["BIRD", "BIRK", "BIKF", "EKVG", "BIIS", "BIVM", "BIAR", "BGSF"]
api_uri = "http://localhost:5000/api/update-positions"

vatsim_data_urls = data_filter.getDataUrls(scraper.grab_json(vatsim_status_url))
selected_data_url = random.choice(vatsim_data_urls)

print(f"""\nVATSIM Data Scraper v{version}
By Liam P\n""")

print(f"Getting data from: {selected_data_url}")

json_data = data_filter.import_json(scraper.grab_json(selected_data_url))
atc_clients = data_filter.filter_atc(json_data)
stations_json = data_filter.filter_iceland_pos(atc_clients, filter_positions)
file_manager.write(stations_json)

api_handler.put(api_uri, stations_json)

# Testing
# print(scraper.grab_json(selected_data_url))