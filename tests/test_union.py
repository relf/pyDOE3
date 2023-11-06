import unittest
from pyDOE3.doe_union import union
import numpy as np


class TestUnion(unittest.TestCase):
    def test_union1(self):
        expected = [[1.0, 0.0], [0.0, 1.0], [2.0, 0.0], [0.0, 2.0]]
        actual = union(np.eye(2), 2 * np.eye(2))
        np.testing.assert_allclose(actual, expected)
