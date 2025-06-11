from pygmc import GMC800
import time
import struct

DEVICE_PATH = '/dev/ttyUSB0'

def main():
    try:
        gmc = GMC800(DEVICE_PATH)
        print("Connected to GMC-800.")
    except Exception as e:
        print(f"Failed to connect: {e}")
        return

    try:
        while True:
            try:
                cpm = gmc.get_cpm()
                usv = gmc.get_usv_h()
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{timestamp}] CPM: {cpm}, µSv/h: {usv}")
            except struct.error as e:
                print(f"[WARN] Incomplete data received: {e}")
            except Exception as e:
                print(f"[ERROR] Unexpected error: {e}")
            time.sleep(2)
    except KeyboardInterrupt:
        print("Exiting...")

if __name__ == '__main__':
    main()
