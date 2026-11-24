![IA Software · Cutting-Edge Technology](../../assets/ia-software-banner.png)

# Web SCADA and Industrial Interface

SCADA application and modular interface

## Objective

Display and log Siemens S7 PLC signals and operate inspection services from a web interface.

## Implementation

The SCADA application stores historical data and streams status changes and alarms over WebSocket. It includes operator and administrator roles, CSV export, and a PLC simulator for testing the interface. A separate modular React interface launches standalone Python applications through Flask.

## Technologies

Python, FastAPI, WebSocket, SQLite, python-snap7, React, Flask.

## Run the demo

```sh
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Open [the simulated dashboard](http://localhost:8000/). The sample speed changes every two seconds and the alarm activates above 75 m/min. The endpoint `/api/tags` exposes the current synthetic signals.

[Back to the portfolio](../../README.md)
