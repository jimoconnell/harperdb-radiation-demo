import requests
import time
import serial
import pynmea2
from pygmc import GMC800

DEVICE_PATH = '/dev/ttyUSB0'
GPS_PATH = '/dev/ttyACM0'
ENDPOINT = 'http://127.0.0.1:3000/radiation'

gmc = GMC800(DEVICE_PATH)
gps_serial = serial.Serial(GPS_PATH, 9600, timeout=1)
print("Connected to GMC-800 and GPS.")

def get_gps():
    while True:
        line = gps_serial.readline().decode('ascii', errors='replace')
        if line.startswith('$GPGGA'):
            try:
                msg = pynmea2.parse(line)
                return msg.latitude, msg.longitude
            except pynmea2.nmea.ChecksumError:
                continue

try:
    while True:
        try:
            cpm = gmc.get_cpm()
            usv = gmc.get_usv_h()
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            lat, lon = get_gps()

            if 0 < cpm < 10000:
                payload = {
                    "id": f"gmc_{int(time.time())}",
                    "timestamp": timestamp,
                    "cpm": cpm,
                    "usv": usv,
                    "lat": lat,
                    "lon": lon,
                    "source": "pi5-lab",
                    "user": "jim"
                }
                response = requests.post(ENDPOINT, json=payload)
                print(f"[{timestamp}] Sent: CPM={cpm}, µSv/h={usv}, Lat={lat}, Lon={lon}, status={response.status_code}")
            else:
                print(f"[{timestamp}] Skipped bogus CPM: {cpm}")

        except Exception as e:
            print(f"[ERROR] {e}")

        time.sleep(5)
except KeyboardInterrupt:
    print("Stopped.")