import unittest
import numpy as np
from pyDOE3.doe_optimal import (
    optimal_design,
    generate_candidate_set,
    build_design_matrix,
    build_uniform_moment_matrix,
    sequential_dykstra,
    simple_exchange_wynn_mitchell,
    fedorov,
    modified_fedorov,
    detmax,
    d_optimality,
    a_optimality,
    i_optimality,
    c_optimality,
    e_optimality,
    g_optimality,
    v_optimality,
    s_optimality,
    t_optimality,
    d_efficiency,
    a_efficiency,
    information_matrix,
    criterion_value,
)


class TestOptimalDesign(unittest.TestCase):
    def setUp(self):
        np.random.seed(42)
        self.candidates_2d = generate_candidate_set(
            n_factors=2, n_levels=5, bounds=(-1, 1)
        )
        self.candidates_3d = generate_candidate_set(
            n_factors=3, n_levels=3, bounds=(-1, 1)
        )

    def test_generate_candidate_set_2d(self):
        expected_shape = (25, 2)
        actual = generate_candidate_set(n_factors=2, n_levels=5, bounds=(-1, 1))
        self.assertEqual(actual.shape, expected_shape)
        self.assertTrue(np.all(actual >= -1))
        self.assertTrue(np.all(actual <= 1))

    def test_generate_candidate_set_3d(self):
        expected_shape = (27, 3)
        actual = generate_candidate_set(n_factors=3, n_levels=3, bounds=(-1, 1))
        self.assertEqual(actual.shape, expected_shape)
        self.assertTrue(np.all(actual >= -1))
        self.assertTrue(np.all(actual <= 1))

    def test_generate_candidate_set_random(self):
        np.random.seed(42)
        actual = generate_candidate_set(
            n_factors=2, n_levels=3, bounds=(-1, 1), grid_type="uniform_random"
        )
        expected_shape = (9, 2)
        self.assertEqual(actual.shape, expected_shape)
        self.assertTrue(np.all(actual >= -1))
        self.assertTrue(np.all(actual <= 1))

    def test_build_design_matrix_linear(self):
        points = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
        expected = np.array(
            [
                [1, 0, 0],
                [1, 1, 0],
                [1, 0, 1],
                [1, 1, 1],
            ]
        )
        actual = build_design_matrix(points, degree=1)
        np.testing.assert_allclose(actual, expected)

    def test_build_design_matrix_quadratic(self):
        points = np.array([[0, 0], [1, 1]])
        expected = np.array(
            [
                [1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1],
            ]
        )
        actual = build_design_matrix(points, degree=2)
        np.testing.assert_allclose(actual, expected)

    def test_information_matrix_normalized(self):
        X = np.array([[1, 0], [1, 1], [1, -1]])
        expected = np.array([[1, 0], [0, 2 / 3]])
        actual = information_matrix(X, normalized=True)
        np.testing.assert_allclose(actual, expected)

    def test_information_matrix_unnormalized(self):
        X = np.array([[1, 0], [1, 1], [1, -1]])
        expected = np.array([[3, 0], [0, 2]])
        actual = information_matrix(X, normalized=False)
        np.testing.assert_allclose(actual, expected)

    def test_information_matrix_augmented(self):
        X = np.array([[1, 0], [1, 1]])
        X0 = np.array([[1, 0], [1, 1], [1, -1]])
        alpha = 0.5

        H = X.T @ X
        H0 = (X0.T @ X0) / 3
        expected = (H + alpha * H0) / 2

        actual = information_matrix(X, normalized=True, alpha=alpha, X0=X0)
        np.testing.assert_allclose(actual, expected)

    def test_d_optimality(self):
        M = np.array([[2, 0], [0, 2]])
        expected = 4.0
        actual = d_optimality(M)
        self.assertAlmostEqual(actual, expected)

    def test_a_optimality(self):
        M = np.array([[2, 0], [0, 2]])
        expected = -1.0
        actual = a_optimality(M)
        self.assertAlmostEqual(actual, expected)

    def test_i_optimality(self):
        M_X = np.array([[2, 0], [0, 2]])
        moment_matrix = np.array([[1, 0], [0, 1]])
        expected = -1.0
        actual = i_optimality(M_X, moment_matrix)
        self.assertAlmostEqual(actual, expected)

    def test_c_optimality(self):
        M = np.array([[2, 0], [0, 2]])
        c = np.array([1, 0])
        expected = -0.5
        actual = c_optimality(M, c)
        self.assertAlmostEqual(actual, expected)

    def test_e_optimality(self):
        M = np.array([[3, 1], [1, 2]])
        eigenvals = np.linalg.eigvalsh(M)
        expected = float(np.min(eigenvals))
        actual = e_optimality(M)
        self.assertAlmostEqual(actual, expected)

    def test_g_optimality(self):
        M = np.array([[2, 0], [0, 2]])
        candidates = np.array([[1, 0], [0, 1], [1, 1]])
        _M_inv = np.linalg.inv(M)
        _variances = np.array([0.5, 0.5, 1.0])
        expected = -1.0
        actual = g_optimality(M, candidates)
        self.assertAlmostEqual(actual, expected)

    def test_v_optimality(self):
        M = np.array([[2, 0], [0, 2]])
        test_points = np.array([[1, 0], [0, 1]])
        expected = -0.5
        actual = v_optimality(M, test_points)
        self.assertAlmostEqual(actual, expected)

    def test_s_optimality(self):
        M = np.array([[4, 0], [0, 1]])
        det_M = 4.0
        col_rms = np.sqrt([4, 1])
        expected = det_M / np.prod(col_rms)
        actual = s_optimality(M)
        self.assertAlmostEqual(actual, expected)

    def test_t_optimality(self):
        X = np.array([[1, 0], [1, 1], [1, -1]])
        model_diff_subset = np.array([1, 0, -1])

        H = X.T @ X
        H_inv = np.linalg.inv(H)
        P = X @ H_inv @ X.T
        d = model_diff_subset.reshape(-1, 1)
        expected = float((d.T @ P @ d).item())

        actual = t_optimality(X, model_diff_subset)
        self.assertAlmostEqual(actual, expected)

    def test_d_efficiency(self):
        X = np.array([[1, 0], [1, 1], [1, -1]])
        M = information_matrix(X, normalized=True)
        p = X.shape[1]
        expected = 100.0 * (np.linalg.det(M) ** (1.0 / p))
        actual = d_efficiency(X)
        self.assertAlmostEqual(actual, expected)

    def test_a_efficiency(self):
        X = np.array([[1, 0], [1, 1], [1, -1]])
        M = information_matrix(X, normalized=True)
        p = X.shape[1]
        expected = 100.0 * (p / np.trace(np.linalg.inv(M)))
        actual = a_efficiency(X)
        self.assertAlmostEqual(actual, expected)

    def test_sequential_dykstra_algorithm(self):
        design = sequential_dykstra(
            self.candidates_2d, n_points=6, degree=2, criterion="D", alpha=0.01
        )
        self.assertEqual(design.shape, (6, 2))
        self.assertTrue(np.all(design >= -1))
        self.assertTrue(np.all(design <= 1))

    def test_simple_exchange_algorithm(self):
        design = simple_exchange_wynn_mitchell(
            self.candidates_2d,
            n_points=6,
            degree=2,
            criterion="D",
            alpha=0.01,
            max_iter=50,
        )
        self.assertEqual(design.shape, (6, 2))
        self.assertTrue(np.all(design >= -1))
        self.assertTrue(np.all(design <= 1))

    def test_fedorov_algorithm(self):
        design = fedorov(
            self.candidates_2d,
            n_points=6,
            degree=2,
            criterion="D",
            alpha=0.01,
            max_iter=50,
        )
        self.assertEqual(design.shape, (6, 2))
        self.assertTrue(np.all(design >= -1))
        self.assertTrue(np.all(design <= 1))

    def test_modified_fedorov_algorithm(self):
        design = modified_fedorov(
            self.candidates_2d,
            n_points=6,
            degree=2,
            criterion="D",
            alpha=0.01,
            max_iter=50,
        )
        self.assertEqual(design.shape, (6, 2))
        self.assertTrue(np.all(design >= -1))
        self.assertTrue(np.all(design <= 1))

    def test_detmax_algorithm(self):
        design = detmax(
            self.candidates_2d,
            n_points=6,
            degree=2,
            criterion="D",
            alpha=0.01,
            max_iter=50,
        )
        self.assertEqual(design.shape, (6, 2))
        self.assertTrue(np.all(design >= -1))
        self.assertTrue(np.all(design <= 1))

    def test_algorithm_with_a_optimality(self):
        design = detmax(
            self.candidates_2d, n_points=6, degree=2, criterion="A", alpha=0.01
        )
        self.assertEqual(design.shape, (6, 2))

    def test_algorithm_with_i_optimality(self):
        design = detmax(
            self.candidates_2d, n_points=6, degree=2, criterion="I", alpha=0.01
        )
        self.assertEqual(design.shape, (6, 2))

    def test_optimal_design_d_criterion(self):
        design, info = optimal_design(
            candidates=self.candidates_2d,
            n_points=8,
            degree=2,
            criterion="D",
            method="detmax",
            alpha=0.01,
        )

        self.assertEqual(design.shape, (8, 2))
        self.assertEqual(info["criterion"], "D")
        self.assertEqual(info["method"], "detmax")
        self.assertEqual(info["alpha"], 0.01)
        self.assertIn("score", info)
        self.assertIn("D_eff", info)
        self.assertIn("A_eff", info)
        self.assertIn("p_columns", info)
        self.assertIn("n_runs", info)

    def test_optimal_design_a_criterion(self):
        design, info = optimal_design(
            candidates=self.candidates_2d,
            n_points=8,
            degree=2,
            criterion="A",
            method="sequential",
            alpha=0.01,
        )

        self.assertEqual(design.shape, (8, 2))
        self.assertEqual(info["criterion"], "A")
        self.assertEqual(info["method"], "sequential")

    def test_optimal_design_i_criterion(self):
        design, info = optimal_design(
            candidates=self.candidates_2d,
            n_points=8,
            degree=2,
            criterion="I",
            method="simple_exchange",
            alpha=0.01,
        )

        self.assertEqual(design.shape, (8, 2))
        self.assertEqual(info["criterion"], "I")
        self.assertEqual(info["method"], "simple_exchange")

    def test_optimal_design_all_methods(self):
        methods = [
            "sequential",
            "simple_exchange",
            "fedorov",
            "modified_fedorov",
            "detmax",
        ]

        for method in methods:
            with self.subTest(method=method):
                design, info = optimal_design(
                    candidates=self.candidates_2d,
                    n_points=6,
                    degree=1,
                    criterion="D",
                    method=method,
                    max_iter=20,
                )

                self.assertEqual(design.shape, (6, 2))
                self.assertEqual(info["method"], method)
                self.assertGreater(info["D_eff"], 80)
                self.assertGreater(info["A_eff"], 80)

    def test_criterion_value_function(self):
        X = build_design_matrix(self.candidates_2d[:6], degree=2)
        X0 = build_design_matrix(self.candidates_2d, degree=2)

        criteria = ["D", "A", "I", "E", "S"]
        for criterion in criteria:
            with self.subTest(criterion=criterion):
                score = criterion_value(X, criterion, X0, alpha=0.01)
                self.assertIsInstance(score, float)
                self.assertFalse(np.isnan(score))
                self.assertFalse(np.isinf(score))

    def test_build_uniform_moment_matrix(self):
        X0 = build_design_matrix(self.candidates_2d, degree=2)
        moment_matrix = build_uniform_moment_matrix(X0)

        expected_shape = (X0.shape[1], X0.shape[1])
        self.assertEqual(moment_matrix.shape, expected_shape)

        np.testing.assert_allclose(moment_matrix, moment_matrix.T)

        eigenvals = np.linalg.eigvalsh(moment_matrix)
        self.assertTrue(np.all(eigenvals >= -1e-10))

    def test_higher_degree_models(self):
        design, info = optimal_design(
            candidates=self.candidates_2d,
            n_points=12,
            degree=3,
            criterion="D",
            method="detmax",
        )

        X = build_design_matrix(design, degree=3)
        expected_params = 10
        self.assertEqual(X.shape[1], expected_params)
        self.assertEqual(info["p_columns"], expected_params)

    def test_3d_design_space(self):
        design, info = optimal_design(
            candidates=self.candidates_3d,
            n_points=15,
            degree=2,
            criterion="D",
            method="detmax",
        )

        self.assertEqual(design.shape, (15, 3))
        self.assertTrue(np.all(design >= -1))
        self.assertTrue(np.all(design <= 1))

        X = build_design_matrix(design, degree=2)
        expected_params = 10
        self.assertEqual(X.shape[1], expected_params)

    def test_error_handling_insufficient_points(self):
        try:
            design, info = optimal_design(
                candidates=self.candidates_2d[:10],
                n_points=3,
                degree=1,
                criterion="D",
                method="sequential",
            )
            self.assertEqual(design.shape, (3, 2))
        except Exception as e:
            self.assertIn("singular", str(e).lower())

    def test_error_handling_unknown_criterion(self):
        with self.assertRaises(ValueError):
            criterion_value(
                build_design_matrix(self.candidates_2d[:6], degree=2),
                "UNKNOWN",
                build_design_matrix(self.candidates_2d, degree=2),
            )

    def test_error_handling_unknown_method(self):
        with self.assertRaises(ValueError):
            optimal_design(
                candidates=self.candidates_2d,
                n_points=6,
                degree=2,
                criterion="D",
                method="unknown_method",
            )

    def test_reproducibility(self):
        np.random.seed(42)
        design1, info1 = optimal_design(
            candidates=self.candidates_2d,
            n_points=8,
            degree=2,
            criterion="D",
            method="detmax",
        )

        np.random.seed(42)
        design2, info2 = optimal_design(
            candidates=self.candidates_2d,
            n_points=8,
            degree=2,
            criterion="D",
            method="detmax",
        )

        np.testing.assert_allclose(design1, design2)
        self.assertAlmostEqual(info1["score"], info2["score"])

    def test_augmentation_parameter_effect(self):
        design1, info1 = optimal_design(
            candidates=self.candidates_2d,
            n_points=8,
            degree=2,
            criterion="D",
            method="sequential",
            alpha=0.0,
        )

        design2, info2 = optimal_design(
            candidates=self.candidates_2d,
            n_points=8,
            degree=2,
            criterion="D",
            method="sequential",
            alpha=0.1,
        )

        self.assertFalse(np.allclose(design1, design2))

    def test_efficiency_bounds(self):
        design, info = optimal_design(
            candidates=self.candidates_2d,
            n_points=10,
            degree=2,
            criterion="D",
            method="detmax",
        )

        self.assertGreater(info["D_eff"], 40)
        self.assertGreater(info["A_eff"], 20)
        self.assertLessEqual(info["D_eff"], 100)
        self.assertLessEqual(info["A_eff"], 100)


if __name__ == "__main__":
    unittest.main()
