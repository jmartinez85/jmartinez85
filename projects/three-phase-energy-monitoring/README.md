![IA Software · Cutting-Edge Technology](../../assets/ia-software-banner.png)

# Three-Phase Energy Monitoring

Data acquisition and analysis tools

## Objective

Record measurements from a three-phase solar power meter and prepare them for analysis.

## Implementation

The monitor reads and logs measurements over Modbus. An MQTT subscriber collects readings through a message broker, and a Jupyter notebook explores forecasting on the resulting time series.

## Technologies

Python, Modbus, MQTT, pandas, Jupyter.

## Run the demo

```sh
python three_phase_monitor.py examples/three_phase_readings.csv
python mqtt_subscriber_powermeter.py --sample examples/mqtt-reading.json
```

The replay prints aggregate power for 24 synthetic readings. The offline MQTT sample gives `3.7` kW. Open [the notebook](notebooks/forecast_demo.ipynb) to run a moving-average forecast. To receive messages from your own test broker, install `requirements.txt`, set the variables in `.env.example` as needed, and run the subscriber without `--sample`.

[Back to the portfolio](../../README.md)
