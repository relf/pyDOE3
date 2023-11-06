import unittest
from pyDOE3.doe_composite import ccdesign
import numpy as np


class TestComposite(unittest.TestCase):
    def test_composite1(self):
        expected = [
            [-1.0, -1.0, -1.0],
            [1.0, -1.0, -1.0],
            [-1.0, 1.0, -1.0],
            [1.0, 1.0, -1.0],
            [-1.0, -1.0, 1.0],
            [1.0, -1.0, 1.0],
            [-1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0],
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
            [-1.82574186, 0.0, 0.0],
            [1.82574186, 0.0, 0.0],
            [0.0, -1.82574186, 0.0],
            [0.0, 1.82574186, 0.0],
            [0.0, 0.0, -1.82574186],
            [0.0, 0.0, 1.82574186],
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
        ]
        actual = ccdesign(3)
        np.testing.assert_allclose(actual, expected)
