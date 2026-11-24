import unittest

import numpy as np

from demo.seam_detection import find_seam


class SeamTests(unittest.TestCase):
    def test_finds_bright_column(self):
        image = np.zeros((20, 32), dtype=np.uint8)
        image[:, 14] = 200
        self.assertEqual(find_seam(image), 14)

    def test_rejects_empty_input(self):
        with self.assertRaises(ValueError):
            find_seam(np.empty((0, 16), dtype=np.uint8))
