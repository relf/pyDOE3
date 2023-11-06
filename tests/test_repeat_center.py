import unittest
from pyDOE3.doe_repeat_center import repeat_center
import numpy as np


class TestRepeatCenter(unittest.TestCase):
    def test_repeat_center1(self):
        expected = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
        actual = repeat_center(3, 2)
        np.testing.assert_allclose(actual, expected)
