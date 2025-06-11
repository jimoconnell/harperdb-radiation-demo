# HarperDB Radiation Monitoring Demo

This project connects a USB Geiger counter (GQ GMC-800) to a live dashboard powered by HarperDB Cloud. It polls radiation data in real-time from a Raspberry Pi and displays it in a browser using Chart.js.

It started as a simple “Hello World” test of HarperDB — and evolved into a full working prototype for sensor-driven data ingestion and visualization.

👉 Read the full write-up here:  
**[From Hello World to Radiation Monitoring: Exploring HarperDB with a Practical Application](https://mmdc.net/from-hello-world-to-radiation-monitoring-exploring-harperdb-with-a-practical-application/)**

---

## Features

- 📡 Live radiation readings from a GMC-800 Geiger counter
- 🌐 HarperDB Cloud as the data backend (REST API via Express)
- 📊 Real-time Chart.js frontend dashboard
- 🧪 Simple status color indicator (Normal / Elevated / High)
- 🐍 Python script on Raspberry Pi pushes data every 5 seconds

---

## Project Structure

```
harperdb-radiation-demo/
├── index.js              # Node.js backend (Express + routes)
├── public/index.html     # Frontend chart + current reading
├── geiger_counter/
│   ├── read_geiger.py    # Reads data from GMC-800
│   └── send_to_harper.py # Pushes data to Node backend
├── package.json
├── .gitignore
├── README.md
```

---

## Requirements

- Raspberry Pi with Python 3.10+ and USB access
- GQ GMC-800 Geiger counter
- A HarperDB Cloud account (free tier works)

---

## Setup

### 1. Install Node dependencies

```bash
npm install
```

### 2. Run the backend

```bash
node index.js
```

By default, it runs on `http://localhost:3000` and serves the dashboard at `/`.

### 3. Run the Geiger counter script on your Pi

```bash
cd geiger_counter
source path/to/venv/bin/activate  # if using a virtual environment
python send_to_harper.py
```

Be sure to update the `ENDPOINT` in `send_to_harper.py` to point to your Node server.

---

## Demo

Once everything is running, visit:

```
http://<your-server>:3000
```

You’ll see a live-updating chart and current radiation reading.

---

## Notes

- The frontend polls every 1 second from `/radiation/list`
- You can adjust polling or thresholds in `index.html`
- The backend inserts data into the `tasks.radiation` table in your HarperDB Cloud instance

---

## License

MIT

---

Project by [Jim O’Connell](https://github.com/jimoconnell)  
Blog: [mmdc.net](https://mmdc.net)
