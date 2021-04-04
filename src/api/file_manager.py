import json
import os

def read():
    with open("./data/positions.json", "r") as positions_data:
        data = json.loads(positions_data.read())

    return data

def write(data):
    with open("data/positions.json", "w") as write_file:
        json.dump(data, write_file)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(f"Successfully wrote to {dir_path}\data\positions.json.")
    return "Success!"

if __name__ == "__main__":
    print(read())