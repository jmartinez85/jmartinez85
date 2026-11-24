const bounds = (value, low, high) => Math.min(high, Math.max(low, value));
const home = () => ({ pan: 0, tilt: 0, zoom: 1 });

export class MockCamera {
  constructor() {
    this.position = home();
  }

  command(action) {
    const position = this.position;
    switch (action) {
      case "left": position.pan = bounds(position.pan - 10, -90, 90); break;
      case "right": position.pan = bounds(position.pan + 10, -90, 90); break;
      case "up": position.tilt = bounds(position.tilt + 10, -45, 45); break;
      case "down": position.tilt = bounds(position.tilt - 10, -45, 45); break;
      case "zoom-in": position.zoom = bounds(position.zoom + 1, 1, 5); break;
      case "zoom-out": position.zoom = bounds(position.zoom - 1, 1, 5); break;
      case "home": this.position = home(); break;
      default: throw new RangeError("Unsupported camera command");
    }
    return this.position;
  }
}
