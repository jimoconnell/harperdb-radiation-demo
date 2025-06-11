import requests
import time
from pygmc import GMC800

DEVICE_PATH = '/dev/ttyUSB0'
# ENDPOINT = 'http://192.168.1.223:3000/radiation'  # Node app on the Mac
ENDPOINT = 'http://127.0.0.1:3000/radiation'  # Node app on this machine

gmc = GMC800(DEVICE_PATH)
print("Connected to GMC-800.")

try:
    while True:
        try:
            cpm = gmc.get_cpm()
            usv = gmc.get_usv_h()
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

            if 0 < cpm < 10000:
                payload = {
                    "id": f"gmc_{int(time.time())}",
                    "timestamp": timestamp,
                    "cpm": cpm,
                    "usv": usv,
                    "source": "pi5-lab"
                }
                response = requests.post(ENDPOINT, json=payload)
                print(f"[{timestamp}] Sent: CPM={cpm}, µSv/h={usv}, status={response.status_code}")
            else:
                print(f"[{timestamp}] Skipped bogus CPM: {cpm}")

        except Exception as e:
            print(f"[ERROR] {e}")

        time.sleep(5)
except KeyboardInterrupt:
    print("Stopped.")
