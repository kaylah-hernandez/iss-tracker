import requests

def fetch_position():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    data = response.json()

    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]
    timestamp = data["timestamp"]

    print(f"ISS Position")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
    print(f"Timestamp: {timestamp}")

if __name__ == "__main__":
    fetch_position()