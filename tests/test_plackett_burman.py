import unittest
from pyDOE3 import pbdesign
import numpy as np


class TestPlackettBurman(unittest.TestCase):
    def test_plackett_burman1(self):
        expected = [
            [-1.0, -1.0, 1.0],
            [1.0, -1.0, -1.0],
            [-1.0, 1.0, -1.0],
            [1.0, 1.0, 1.0],
        ]
        actual = pbdesign(3)
        np.testing.assert_allclose(actual, expected)

    def test_plackett_burman2(self):
        expected = [
            [-1.0, -1.0, 1.0, -1.0, 1.0],
            [1.0, -1.0, -1.0, -1.0, -1.0],
            [-1.0, 1.0, -1.0, -1.0, 1.0],
            [1.0, 1.0, 1.0, -1.0, -1.0],
            [-1.0, -1.0, 1.0, 1.0, -1.0],
            [1.0, -1.0, -1.0, 1.0, 1.0],
            [-1.0, 1.0, -1.0, 1.0, -1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0],
        ]
        actual = pbdesign(5)
        np.testing.assert_allclose(actual, expected)
