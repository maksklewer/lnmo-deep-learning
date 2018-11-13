import unittest
from unittest import TestCase
from Tasks.Task001 import MatrixCalculator

import numpy as np


class TestTask001(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calculator = MatrixCalculator()

    def test_sum_normal(self):
        result = self.calculator.sum(np.array([[1, 1], [2, 2]]), np.array([[1, 1], [2, 2]]))
        np.testing.assert_array_equal(result, np.array([[2, 2], [4, 4]]))

    def test_sum_error(self):
        with self.assertRaises(TypeError):
            self.calculator.sum(1, 2)

    def test_mult_normal(self):
        result = self.calculator.mult(np.array([[1, 1], [2, 2]]), np.array([[1, 1], [2, 2]]))
        np.testing.assert_array_equal(result, np.array([[3, 3], [6, 6]]))

    def test_mult_dif(self):
        result = self.calculator.mult(np.array([[1, 1], [2, 2]]), np.array([[1], [1]]))
        np.testing.assert_array_equal(result, np.array([[2], [4]]))

    def test_mult_error(self):
        with self.assertRaises(TypeError):
            self.calculator.mult(1, 1)
