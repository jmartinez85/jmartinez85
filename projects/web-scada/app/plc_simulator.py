import time


class PLCSimulator:
    def __init__(self, samples, limit):
        self.samples = samples
        self.limit = limit
        self.started = time.monotonic()

    def read(self):
        tick = int((time.monotonic() - self.started) / 2)
        speed = self.samples[tick % len(self.samples)]
        return {"line_speed": speed, "running": True, "alarm": speed > self.limit}
