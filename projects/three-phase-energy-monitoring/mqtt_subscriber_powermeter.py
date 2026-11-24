"""Print aggregate power for the demo JSON schema received over MQTT."""

import argparse
import json
import os
from pathlib import Path

from three_phase_monitor import summarize


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sample", type=Path, help="Validate a JSON sample offline")
    args = parser.parse_args()
    if args.sample:
        print(json.dumps(summarize(json.loads(args.sample.read_text()))))
        return

    import paho.mqtt.client as mqtt

    topic = os.environ.get("MQTT_TOPIC", "demo/energy")
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

    def connected(client, userdata, flags, reason, properties):
        if reason.is_failure:
            print(f"Broker rejected connection: {reason}")
        else:
            client.subscribe(topic)

    def received(client, userdata, message):
        try:
            print(json.dumps(summarize(json.loads(message.payload))), flush=True)
        except (KeyError, TypeError, ValueError) as error:
            print(f"Invalid sample: {error}", flush=True)

    client.on_connect = connected
    client.on_message = received
    client.connect(os.environ.get("MQTT_HOST", "localhost"), int(os.environ.get("MQTT_PORT", "1883")))
    client.loop_forever()


if __name__ == "__main__":
    main()
