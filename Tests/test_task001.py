import unittest
from unittest import TestCase
from Tasks.Task001 import MatrixCalculator

import numpy as np;


class TestTask001(TestCase):
    def test_sum_normal(self):
        calculator = MatrixCalculator()
        result = calculator.sum(np.matrix('1 1; 2 2'), np.matrix('1 1;2 2'))
        np.testing.assert_array_equal(result, np.matrix('2 2;4 4'))

    def test_sum_dif(self):
        calculator = MatrixCalculator()
        result = calculator.sum(np.matrix('1 1; 2 2'), np.matrix('1 1'))
        np.testing.assert_array_equal(result, np.matrix('2 2;2 2'))

    def test_sum_error(self):
        calculator = MatrixCalculator()
        result = calculator.sum(1, 2)
        self.assertRaises(Exception)

    def test_mult_normal(self):
        calculator = MatrixCalculator()
        result = calculator.mult(np.matrix('1 1; 2 2'), np.matrix('1 1;2 2'))
        np.testing.assert_array_equal(result, np.matrix('3 3;6 6'))

    def test_mult_dif(self):
        calculator = MatrixCalculator()
        result = calculator.mult(np.matrix('1 1; 2 2'), np.matrix('1 1'))
        np.testing.assert_array_equal(result, np.matrix('2 2;4 4'))

    def test_mult_error(self):
        calculator = MatrixCalculator()
        result = calculator.mult(1, 1)
        self.assertRaises(Exception)


if __name__ == '__main__':
    unittest.main()
