![IA Software · Cutting-Edge Technology](../../assets/ia-software-banner.png)

# Automated Cold-Storage Warehouse

Industrial controls integration and commissioning

## Objective

Coordinate a continuous freezing tunnel, pallet handling, and automated storage and retrieval. The warehouse needed to recover interrupted sequences and keep the supervisory software informed about equipment status and completed movements.

## Implementation

- Developed the main Siemens S7 PLC control logic for equipment sequencing, interlocks, drive coordination, and recovery after interruptions.
- Integrated the warehouse supervisory software over OPC to exchange storage and retrieval commands, acknowledgments, alarms, and equipment states.
- Configured and commissioned the industrial radio link between the fixed network and the stacker crane's mobile controller. Commissioning covered pallet movements, crane positioning, freezing tunnel cycles, and rejection of pallets that failed dimensional checks.

## Technologies

Siemens S7-1516-3 PN/DP, TIA Portal, OPC, industrial Ethernet, Ubiquiti Loco M5, Siemens SINAMICS.

[View the warehouse case study and simulation](https://www.iasoftware.com.ar/projects/warehouse/)

## Run the demo

+[Open the warehouse simulation on GitHub Pages](https://jmartinez85.github.io/jmartinez85/projects/automated-cold-storage-warehouse/demo/).

To run it locally, start `python3 -m http.server 8000 --bind 127.0.0.1` from the portfolio root and open [the local demo](http://localhost:8000/projects/automated-cold-storage-warehouse/demo/).

Select **Store pallet** and advance until the pallet reaches the rack, then retrieve it. The command log shows the acknowledgments. See the [control flow](docs/control-architecture.md).

[Back to the portfolio](../../README.md)
