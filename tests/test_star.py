import unittest
import array as array
from pyDOE3.response_surface_designs import star
import numpy as np


class TestStar(unittest.TestCase):
    def test_star1(self):
        expected = (
            np.array(
                [
                    [-1.0, 0.0, 0.0],
                    [1.0, 0.0, 0.0],
                    [0.0, -1.0, 0.0],
                    [0.0, 1.0, 0.0],
                    [0.0, 0.0, -1.0],
                    [0.0, 0.0, 1.0],
                ]
            ),
            1,
        )
        actual = star(3)
        np.testing.assert_allclose(actual[0], expected[0])
        self.assertEqual(actual[1], expected[1])
