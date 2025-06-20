import requests
import random
import time
from datetime import datetime
import math

ENDPOINT = 'http://127.0.0.1:3000/radiation'

# Reference coordinates (center of your location)
base_lat = 41.23
base_lon = -77.03

def jitter(val, max_miles=100):
    # ~0.0145 degrees lat/lon per mile
    max_deg = max_miles * 0.0145
    return val + random.uniform(-max_deg, max_deg)

def generate_user_id(i):
    return f"user_{str(i).zfill(3)}"

def generate_payload(user_id):
    cpm = random.randint(5, 800)
    usv = round(cpm * 0.0065, 3)  # rough conversion
    lat = jitter(base_lat)
    lon = jitter(base_lon)
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    return {
        "id": f"{user_id}_{int(time.time()*1000)}",
        "timestamp": timestamp,
        "cpm": cpm,
        "usv": usv,
        "lat": lat,
        "lon": lon,
        "source": "simulated",
        "user": user_id
    }

try:
    while True:
        for i in range(100):
            user_id = generate_user_id(i)
            payload = generate_payload(user_id)
            try:
                res = requests.post(ENDPOINT, json=payload)
                print(f"[{payload['timestamp']}] {user_id} - CPM: {payload['cpm']} µSv/h: {payload['usv']} (status: {res.status_code})")
            except Exception as e:
                print(f"[ERROR] {user_id}: {e}")
        time.sleep(1000)  # wait before next round

except KeyboardInterrupt:
    print("Simulation stopped.")