# Iceland FIR ATC Positions API

For the Iceland FIR on the VATSIM network.

## Purpose

This script will check the datafeed from VATSIM and filter it down to just displaying controllers who are providing an ATC service in the Iceland FIR. (Positions can be changed in `run.py` by editing the `filter_positions` list). The script will then create a JSON file with info on the positions (any data specified in `data_filter.py`).

Only the most controlled aerodromes were added to the list, please feel free to add any aerodromes you feel should be checked and create a PR!

## Requirements

- Flask
- Requests

Grab these libraries using `pip install <lib name>`.

(Please let me know if I have missed anything).

## Running

Ensure you have Python installed (I used 3.8) by navigating to any terminal and typing `python --version`.

### API

The API requires Flask to run. Please keep the terminal window open the whole time you are using the API.

Move into the `src/api` directory (`cd ./src/api`) and run the script with `python api.py`.

### Scraper

Running the scraper will send a PUT request to the API with the JSON file it has built.

Run the scraper by moving to the scraper directory (in a different terminal window) `cd ./src/scraper` and run it using `python run.py`.

To ensure the operation was a success, check the `./src/api/data/positions.json` file. Make sure it matches the `./src/scraper/data/positions.json` file.

## Data

The data is provided by [VATSIM](https://www.vatsim.net/).
