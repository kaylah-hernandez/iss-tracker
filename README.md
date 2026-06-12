# ISS Tracker 🛰️

A Python CLI tool that fetches the real-time position of the International Space Station, logs each sighting locally, and displays your history in a formatted table.

## Features

- Fetches live ISS position from the Open Notify API
- Logs each sighting to a local JSON file with a timestamp
- Displays your last 5 sightings in a clean table

## Requirements

- Python 3
- requests

## Installation

Clone the repository:

```bash
git clone git@github.com:kaylah-hernandez/iss-tracker.git
cd iss-tracker
```

Install dependencies:

```bash
pip3 install requests
```

## Usage

Fetch the current ISS position and log it:

```bash
python3 tracker.py
```

View your sighting history:

```bash
python3 history.py
```

## Example Output

```
ISS Position
Latitude:  25.1296
Longitude: 4.3089
Timestamp: 1781241945
Sighting logged. Total sightings: 6

#     Latitude     Longitude    Recorded At
---------------------------------------------
1     -12.9030     -24.7247     2026-06-12 01:13:01
2     -12.3795     -24.3266     2026-06-12 01:13:11
3     24.0418      3.2882       2026-06-12 01:25:22
4     24.7049      3.9072       2026-06-12 01:25:36
5     25.1296      4.3089       2026-06-12 01:25:45
```

## Built With

- [Open Notify API](http://open-notify.org/) — free real-time ISS position data
- Python standard library — json, os, datetime
- requests — HTTP requests