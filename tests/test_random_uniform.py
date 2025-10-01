import unittest
import numpy as np
from pyDOE3 import random_uniform


class TestRandomUniform(unittest.TestCase):
    def test_random_uniform_basic(self):
        """Test basic functionality of random_uniform."""
        num_points = 10
        dimension = 3

        # Set random seed for reproducibility
        np.random.seed(42)
        result = random_uniform(num_points, dimension)

        # Check output shape
        self.assertEqual(result.shape, (num_points, dimension))

        # Check that all values are in [0, 1)
        self.assertTrue(np.all(result >= 0.0))
        self.assertTrue(np.all(result < 1.0))

    def test_random_uniform_reproducible(self):
        """Test reproducibility with same random seed."""
        expected = np.array(
            [
                [0.37454012, 0.95071431, 0.73199394],
                [0.59865848, 0.15601864, 0.15599452],
                [0.05808361, 0.86617615, 0.60111501],
                [0.70807258, 0.02058449, 0.96990985],
                [0.83244264, 0.21233911, 0.18182497],
            ]
        )

        np.random.seed(42)
        actual = random_uniform(5, 3)

        np.testing.assert_allclose(actual, expected, rtol=1e-6)

    def test_random_uniform_single_point(self):
        """Test with single point."""
        np.random.seed(42)
        result = random_uniform(1, 2)

        self.assertEqual(result.shape, (1, 2))
        self.assertTrue(np.all(result >= 0.0))
        self.assertTrue(np.all(result < 1.0))

    def test_random_uniform_single_dimension(self):
        """Test with single dimension."""
        np.random.seed(42)
        result = random_uniform(5, 1)

        self.assertEqual(result.shape, (5, 1))
        self.assertTrue(np.all(result >= 0.0))
        self.assertTrue(np.all(result < 1.0))

    def test_random_uniform_large_array(self):
        """Test with larger arrays."""
        np.random.seed(42)
        result = random_uniform(100, 10)

        self.assertEqual(result.shape, (100, 10))
        self.assertTrue(np.all(result >= 0.0))
        self.assertTrue(np.all(result < 1.0))

    def test_random_uniform_zero_points(self):
        """Test with zero points."""
        np.random.seed(42)
        result = random_uniform(0, 3)

        self.assertEqual(result.shape, (0, 3))

    def test_random_uniform_zero_dimension(self):
        """Test with zero dimensions."""
        np.random.seed(42)
        result = random_uniform(5, 0)

        self.assertEqual(result.shape, (5, 0))

    def test_random_uniform_distribution_properties(self):
        """Test statistical properties of the uniform distribution."""
        np.random.seed(42)
        result = random_uniform(10000, 1)

        # For uniform distribution on [0, 1):
        # - Mean should be approximately 0.5
        # - Standard deviation should be approximately 1/sqrt(12) ≈ 0.289
        mean = np.mean(result)
        std = np.std(result)

        self.assertAlmostEqual(mean, 0.5, delta=0.02)  # Allow some tolerance
        self.assertAlmostEqual(std, 1 / np.sqrt(12), delta=0.02)

    def test_random_uniform_different_dimensions(self):
        """Test with various dimensions."""
        np.random.seed(42)

        for dim in [1, 2, 5, 10, 20]:
            result = random_uniform(10, dim)
            self.assertEqual(result.shape, (10, dim))
            self.assertTrue(np.all(result >= 0.0))
            self.assertTrue(np.all(result < 1.0))

    def test_random_uniform_different_num_points(self):
        """Test with various numbers of points."""
        np.random.seed(42)

        for num_points in [1, 10, 50, 100]:
            result = random_uniform(num_points, 3)
            self.assertEqual(result.shape, (num_points, 3))
            self.assertTrue(np.all(result >= 0.0))
            self.assertTrue(np.all(result < 1.0))

    def test_random_uniform_independence(self):
        """Test that different calls produce different results (when not seeded)."""
        # Don't set seed for this test
        result1 = random_uniform(10, 3)
        result2 = random_uniform(10, 3)

        # Results should be different (very unlikely to be identical)
        self.assertFalse(np.allclose(result1, result2))

    def test_random_uniform_dtype(self):
        """Test that output has correct data type."""
        np.random.seed(42)
        result = random_uniform(5, 3)

        # Should be float type
        self.assertTrue(np.issubdtype(result.dtype, np.floating))

    def test_random_uniform_bounds_strict(self):
        """Test that values are strictly less than 1.0."""
        np.random.seed(42)
        result = random_uniform(1000, 5)

        # All values should be < 1.0 (not <= 1.0)
        self.assertTrue(np.all(result < 1.0))
        # All values should be >= 0.0
        self.assertTrue(np.all(result >= 0.0))
