import unittest
from pyDOE3.doe_lhs import lhs
from pyDOE3.doe_lhs import _lhsclassic
from pyDOE3.doe_lhs import _lhscentered
from pyDOE3.doe_lhs import _lhsmaximin
import numpy as np


class TestLhs(unittest.TestCase):
    def test_lhs1(self):
        expected = [
            [0.12484671, 0.95539205, 0.24399798],
            [0.53288616, 0.38533955, 0.86703834],
            [0.68602787, 0.31690477, 0.38533151],
        ]
        actual = lhs(3, random_state=42)
        np.testing.assert_allclose(actual, expected)

    def test_lhs2(self):
        expected = [
            [0.06242335, 0.19266575, 0.88202411, 0.89439364],
            [0.19266977, 0.53538985, 0.53030416, 0.49498498],
            [0.71737371, 0.75412607, 0.17634727, 0.71520486],
            [0.63874044, 0.85658231, 0.33676408, 0.31102936],
            [0.43351917, 0.45134543, 0.12199899, 0.53056742],
            [0.93530882, 0.15845238, 0.7386575, 0.09977641],
        ]
        actual = lhs(4, samples=6, random_state=42)
        np.testing.assert_allclose(actual, expected)

    def test_lhs3(self):
        expected = [[0.1, 0.9], [0.5, 0.5], [0.7, 0.1], [0.3, 0.7], [0.9, 0.3]]
        actual = lhs(2, samples=5, criterion="center", random_state=42)
        np.testing.assert_allclose(actual, expected)

    def test_lhs4(self):
        expected = [
            [0.69754389, 0.2997106, 0.96250964],
            [0.10585037, 0.09872038, 0.73157522],
            [0.25351996, 0.65148999, 0.07337204],
            [0.91276926, 0.97873992, 0.42783549],
        ]
        actual = lhs(3, samples=4, criterion="maximin", random_state=42)
        np.testing.assert_allclose(actual, expected)

    def test_lhs5(self):
        expected = [
            [0.4846803, 0.74226839, 0.23305339, 0.97000772],
            [0.98526018, 0.11735023, 0.75803511, 0.20312728],
            [0.10793843, 0.2592547, 0.98299194, 0.72119199],
            [0.25519984, 0.4789763, 0.19305106, 0.12140685],
            [0.63976848, 0.93021541, 0.45869763, 0.40281596],
        ]
        actual = lhs(
            4, samples=5, criterion="correlation", iterations=10, random_state=42
        )
        np.testing.assert_allclose(actual, expected)
