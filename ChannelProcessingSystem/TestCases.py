import unittest
import numpy as np

# Import your functions from the code
from main import array_Y, array_B, metric_b, array_A, array_C

# Create a test case class
class TestYourFunctions(unittest.TestCase):

    # Test array_Y function
    def test_array_Y(self):
        m = 2.0
        c = 1.0
        X = [1, 2, 3]
        expected_result = np.array([3.0, 5.0, 7.0])
        self.assertTrue(np.allclose(array_Y(m, c, X), expected_result))

    # Test array_B function
    def test_array_B(self):
        A = np.array([0.5, 1.0, 1.5])
        Y = np.array([2.0, 3.0, 4.0])
        expected_result = np.array([2.5, 4.0, 5.5])
        self.assertTrue(np.allclose(array_B(A, Y), expected_result))

    # Test metric_b function
    def test_metric_b(self):
        B = np.array([2.5, 4.0, 5.5])
        expected_result = 4.0
        self.assertAlmostEqual(metric_b(B), expected_result)

    # Test array_A function
    def test_array_A(self):
        X = [2, 4, 6]
        expected_result = np.array([0.5, 0.25, 0.16666667])
        self.assertTrue(np.allclose(array_A(X), expected_result))

    # Test array_C function
    def test_array_C(self):
        X = [1, 2, 3]
        b = 4.0
        expected_result = np.array([5.0, 6.0, 7.0])
        self.assertTrue(np.allclose(array_C(X, b), expected_result))

if __name__ == '__main__':
    unittest.main()
