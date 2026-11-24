"""Track bright regions with distance-gated centroid matching."""

import math


class CentroidTracker:
    def __init__(self, max_distance=25):
        self.max_distance = max_distance
        self.positions = {}
        self.next_id = 1

    def update(self, centroids):
        points = [tuple(point) for point in centroids]
        candidates = sorted(
            (math.dist(previous, point), track_id, index)
            for track_id, previous in self.positions.items()
            for index, point in enumerate(points)
        )
        positions = {}
        matched = set()
        for distance, track_id, index in candidates:
            if distance > self.max_distance:
                break
            if track_id not in positions and index not in matched:
                positions[track_id] = points[index]
                matched.add(index)
        for index, point in enumerate(points):
            if index not in matched:
                positions[self.next_id] = point
                self.next_id += 1
        self.positions = positions
        return positions.copy()
