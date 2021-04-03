import scraper
import data_filter

# Vars
version = "1.0.0"
vatsim_data_url = "http://data.vatsim.net"
filter_positions = ["BIRD", "BIRK", "BIKF", "EKVG", "BIIS", "BIVM", "BIAR", "BGSF"]

print(f"""\nVATSIM Data Scraper v{version}
By Liam P\n""")

print(f"Getting data from: {scraper.build_url(vatsim_data_url)}")

json_data = data_filter.import_json(scraper.grab_json(vatsim_data_url))
atc_clients = data_filter.filter_atc(json_data)
stations_json = data_filter.filter_iceland_pos(atc_clients, filter_positions)

print(stations_json)

# Testing
# print(scraper.grab_json(vatsim_data_url))