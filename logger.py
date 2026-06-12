import json
import os
from datetime import datetime

def log_sighting(latitude, longitude, timestamp):
    sighting = {
        "latitude": latitude,
        "longitude": longitude,
        "timestamp": timestamp,
        "recorded_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    if os.path.exists("sightings.json"):
        with open("sightings.json", "r") as f:
            sightings = json.load(f)
    else:
        sightings = []

    sightings.append(sighting)

    with open("sightings.json", "w") as f:
        json.dump(sightings, f, indent=2)

    print(f"Sighting logged. Total sightings: {len(sightings)}")
    