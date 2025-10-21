import json
import os

DATA_FILE = "data/databoss.json"

def load_databoss():
    """Loads boss data from a JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_databoss(databoss):
    """Saves boss data to a JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(databoss, file, indent=4)
 