import scraper
import data_filter
import file_manager
import api_handler

# Vars
version = "1.0.0"
vatsim_data_url = "http://data.vatsim.net"
filter_positions = ["BIRD", "BIRK", "BIKF", "EKVG", "BIIS", "BIVM", "BIAR", "BGSF"]
api_uri = "http://localhost:5000/api/update-positions"

print(f"""\nVATSIM Data Scraper v{version}
By Liam P\n""")

print(f"Getting data from: {scraper.build_url(vatsim_data_url)}")

json_data = data_filter.import_json(scraper.grab_json(vatsim_data_url))
atc_clients = data_filter.filter_atc(json_data)
stations_json = data_filter.filter_iceland_pos(atc_clients, filter_positions)
file_manager.write(stations_json)

api_handler.put(api_uri, stations_json)

# Testing
# print(scraper.grab_json(vatsim_data_url))