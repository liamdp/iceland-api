import json
import os

def write(position_data):
    with open("data/positions.json", "w") as write_file:
        json.dump(position_data, write_file)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(f"Successfully wrote to {dir_path}\data\positions.json.")