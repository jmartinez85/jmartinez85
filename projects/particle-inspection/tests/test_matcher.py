import unittest

from particle_v2.tracker import CentroidTracker


class TrackerTests(unittest.TestCase):
    def test_preserves_identity_when_detection_order_changes(self):
        tracker = CentroidTracker(max_distance=10)
        self.assertEqual(tracker.update([(0, 0), (20, 0)]), {1: (0, 0), 2: (20, 0)})
        self.assertEqual(tracker.update([(19, 0), (1, 0)]), {1: (1, 0), 2: (19, 0)})

    def test_assigns_new_id_outside_gate(self):
        tracker = CentroidTracker(max_distance=5)
        tracker.update([(0, 0)])
        self.assertEqual(tracker.update([(25, 0)]), {2: (25, 0)})
