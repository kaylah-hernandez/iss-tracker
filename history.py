import json
import os

def show_history(limit=5):
    if not os.path.exists("sightings.json"):
        print("No sightings logged yet.")
        return
    
    with open("sightings.json", "r") as f:
        sightings = json.load(f)

    recent = sightings[-limit:]

    print(f"\n{'#':<5} {'Latitude':<12} {'Longitude':<12} {'Recorded At'}")
    print("-" * 45)

    for i, s in enumerate(recent, 1):
        print(f"{i:<5} {s['latitude']:<12} {s['longitude']:<12} {s['recorded_at']}")

if __name__ == "__main__":
    show_history()