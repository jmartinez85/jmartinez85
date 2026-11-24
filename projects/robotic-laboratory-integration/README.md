![IA Software · Cutting-Edge Technology](../../assets/ia-software-banner.png)

# Robotic Laboratory Integration

Industrial robotics, laboratory automation, and plant systems integration

## Objective

Automate the transfer of metal samples between temporary storage, preparation, and analysis stations. Connect the laboratory workflow to plant SCADA and production information systems.

## Implementation

- Integrated FANUC robotic sample handling with the preparation and analytical stations of a Thermo Scientific ARL SMS-3500 cell.
- Developed custom C++ software and interfaces on QNX to exchange laboratory data with plant SCADA and production systems.
- Supported field installation, industrial communications, and commissioning of the automated sample-handling workflow.

## Technologies

FANUC, Thermo Scientific ARL SMS-3500, C++, QNX, SCADA, optical emission spectroscopy (OES), X-ray fluorescence (XRF).

[View the laboratory case study and commissioning footage](https://www.iasoftware.com.ar/projects/lab-robotics/)

## Run the demo

From the portfolio root, run `python3 -m http.server 8000 --bind 127.0.0.1`. Open [the demo](http://localhost:8000/projects/robotic-laboratory-integration/demo/).

Select **Next station** to advance a synthetic metal sample. The sample identifier persists while the station and state change. See the [sample flow](docs/sample-flow.md).

[Back to the portfolio](../../README.md)
