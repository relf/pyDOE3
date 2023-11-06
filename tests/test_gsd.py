import unittest
from pyDOE3.doe_gsd import gsd
import numpy as np


class TestGsd(unittest.TestCase):
    def test_gsd1(self):
        expected = [
            [0, 0, 0],
            [0, 0, 4],
            [0, 1, 1],
            [0, 1, 5],
            [0, 2, 2],
            [0, 3, 3],
            [1, 0, 1],
            [1, 0, 5],
            [1, 1, 2],
            [1, 2, 3],
            [1, 3, 0],
            [1, 3, 4],
            [2, 0, 2],
            [2, 1, 3],
            [2, 2, 0],
            [2, 2, 4],
            [2, 3, 1],
            [2, 3, 5],
        ]
        actual = gsd([3, 4, 6], 4)
        np.testing.assert_allclose(actual, expected)

    def test_gsd2(self):
        expected = [[0, 0], [0, 2], [2, 0], [2, 2], [1, 1], [1, 3]]
        actual = gsd([3, 4], 2, n=2)[0]
        np.testing.assert_allclose(actual, expected)

    def test_gsd3(self):
        expected = [[0, 1], [0, 3], [2, 1], [2, 3], [1, 0], [1, 2]]
        actual = gsd([3, 4], 2, n=2)[1]
        np.testing.assert_allclose(actual, expected)
