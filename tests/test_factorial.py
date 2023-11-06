import unittest
from pyDOE3.doe_factorial import fullfact
from pyDOE3.doe_factorial import ff2n
from pyDOE3.doe_factorial import fracfact
from pyDOE3.doe_factorial import fracfact_by_res
import numpy as np


class TestFactorial(unittest.TestCase):
    def test_factorial1(self):
        expected = [
            [0.0, 0.0, 0.0],
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [1.0, 1.0, 0.0],
            [0.0, 2.0, 0.0],
            [1.0, 2.0, 0.0],
            [0.0, 3.0, 0.0],
            [1.0, 3.0, 0.0],
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 1.0],
            [0.0, 1.0, 1.0],
            [1.0, 1.0, 1.0],
            [0.0, 2.0, 1.0],
            [1.0, 2.0, 1.0],
            [0.0, 3.0, 1.0],
            [1.0, 3.0, 1.0],
            [0.0, 0.0, 2.0],
            [1.0, 0.0, 2.0],
            [0.0, 1.0, 2.0],
            [1.0, 1.0, 2.0],
            [0.0, 2.0, 2.0],
            [1.0, 2.0, 2.0],
            [0.0, 3.0, 2.0],
            [1.0, 3.0, 2.0],
        ]
        actual = fullfact([2, 4, 3])
        np.testing.assert_allclose(actual, expected)

    def test_factorial2(self):
        expected = [
            [-1.0, -1.0, -1.0],
            [1.0, -1.0, -1.0],
            [-1.0, 1.0, -1.0],
            [1.0, 1.0, -1.0],
            [-1.0, -1.0, 1.0],
            [1.0, -1.0, 1.0],
            [-1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0],
        ]
        actual = ff2n(3)
        np.testing.assert_allclose(actual, expected)

    def test_factorial3(self):
        expected = [
            [-1.0, -1.0, 1.0],
            [1.0, -1.0, -1.0],
            [-1.0, 1.0, -1.0],
            [1.0, 1.0, 1.0],
        ]
        actual = fracfact("a b ab")
        np.testing.assert_allclose(actual, expected)

    def test_factorial4(self):
        expected = [
            [-1.0, -1.0, 1.0],
            [1.0, -1.0, -1.0],
            [-1.0, 1.0, -1.0],
            [1.0, 1.0, 1.0],
        ]
        actual = fracfact("A B AB")
        np.testing.assert_allclose(actual, expected)

    def test_factorial5(self):
        expected = [
            [-1.0, -1.0, -1.0, -1.0, -1.0],
            [1.0, -1.0, 1.0, -1.0, 1.0],
            [-1.0, 1.0, 1.0, -1.0, 1.0],
            [1.0, 1.0, -1.0, -1.0, -1.0],
            [-1.0, -1.0, -1.0, 1.0, 1.0],
            [1.0, -1.0, 1.0, 1.0, -1.0],
            [-1.0, 1.0, 1.0, 1.0, -1.0],
            [1.0, 1.0, -1.0, 1.0, 1.0],
        ]
        actual = fracfact("a b -ab c +abc")
        np.testing.assert_allclose(actual, expected)

    def test_factorial6(self):
        expected = [
            [-1.0, -1.0, -1.0, 1.0, 1.0, 1.0],
            [1.0, -1.0, -1.0, -1.0, -1.0, 1.0],
            [-1.0, 1.0, -1.0, -1.0, 1.0, -1.0],
            [1.0, 1.0, -1.0, 1.0, -1.0, -1.0],
            [-1.0, -1.0, 1.0, 1.0, -1.0, -1.0],
            [1.0, -1.0, 1.0, -1.0, 1.0, -1.0],
            [-1.0, 1.0, 1.0, -1.0, -1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        ]
        actual = fracfact_by_res(6, 3)
        np.testing.assert_allclose(actual, expected)
