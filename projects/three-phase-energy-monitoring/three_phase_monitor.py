"""Replay synthetic three-phase meter readings from CSV."""

import argparse
import csv
import json
from pathlib import Path


def summarize(rows):
    phases = ("l1_kw", "l2_kw", "l3_kw")
    return {
        "timestamp": rows["timestamp"],
        "total_kw": round(sum(float(rows[phase]) for phase in phases), 2),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path)
    args = parser.parse_args()
    with args.csv_file.open(newline="") as source:
        for sample in csv.DictReader(source):
            print(json.dumps(summarize(sample)))


if __name__ == "__main__":
    main()
