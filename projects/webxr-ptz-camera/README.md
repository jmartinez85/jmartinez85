![IA Software · Cutting-Edge Technology](../../assets/ia-software-banner.png)

# PTZ Camera Control with WebXR

Desktop application and WebXR prototype

## Objective

View and steer a PTZ camera from a desktop application and explore control in an immersive interface.

## Implementation

The desktop client displays RTSP video, saves camera presets, and translates text instructions into camera operations. The Meta Quest prototype uses Node.js, FFmpeg, and ONVIF to stream video to the browser and handle movement commands.

## Technologies

Python, OpenCV, ONVIF, RTSP, Node.js, FFmpeg, WebXR.

## Run the demo

Run `npm start` with Node.js 20 or newer and open [the camera simulator](http://localhost:8080/). Pan, tilt and zoom move an illustrated target. **Home** resets it. This browser demo exercises the control API against a simulated camera. The case study above describes the separate hardware and immersive prototypes.

[Back to the portfolio](../../README.md)
