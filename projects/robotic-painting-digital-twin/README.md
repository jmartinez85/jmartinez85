![IA Software · Cutting-Edge Technology](../../assets/ia-software-banner.png)

# Robotic Painting Cell and Digital Twin

Robot programming, controls integration, and commissioning

## Objective

Coordinate two KUKA robots, a conveyor, product identification, and spray equipment to paint multiple LPG cylinder and tank formats on an automated line.

## Implementation

- Programmed painting routines and adjusted trajectories for different product formats. Helped commission both KUKA robot systems and coordinated their status and commands with the cell sequence.
- Integrated the Schneider PLC and Magelis HMI with product sensors, conveyor logic, spray actuation, and operator diagnostics.
- Built a RoboDK digital twin with Python tooling to compare robot paths, review product flow, and visualize estimated paint coverage. These studies informed engineering adjustments and commissioning tests.

## Technologies

KUKA KR 16 L6, KRC4, Schneider TM251MESE PLC, Magelis HMI, RoboDK, Python.

[View the painting cell case study and digital twin](https://www.iasoftware.com.ar/projects/robotic-cells/)

## Run the demo

From the portfolio root, run `python3 -m http.server 8000 --bind 127.0.0.1`. Open [the demo](http://localhost:8000/projects/robotic-painting-digital-twin/demo/).

Switch between the **Baseline** and **Alternative** paths and advance one waypoint at a time. The paths use illustrative coordinates. See the [cell architecture](docs/cell-architecture.md).

[Back to the portfolio](../../README.md)
