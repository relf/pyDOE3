import unittest
from pyDOE3.doe_box_behnken import bbdesign
import numpy as np


class TestBoxBehnken(unittest.TestCase):
    def test_box_behnken1(self):
        expected = [
            [-1.0, -1.0, 0.0],
            [1.0, -1.0, 0.0],
            [-1.0, 1.0, 0.0],
            [1.0, 1.0, 0.0],
            [-1.0, 0.0, -1.0],
            [1.0, 0.0, -1.0],
            [-1.0, 0.0, 1.0],
            [1.0, 0.0, 1.0],
            [0.0, -1.0, -1.0],
            [0.0, 1.0, -1.0],
            [0.0, -1.0, 1.0],
            [0.0, 1.0, 1.0],
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
        ]
        actual = bbdesign(3)
        np.testing.assert_allclose(actual, expected)
