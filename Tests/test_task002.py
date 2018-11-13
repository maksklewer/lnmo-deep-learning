import unittest
from unittest import TestCase
from Tasks.Task002 import MatrixPocessor

import numpy as np


class TestDeterminant(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.processor = MatrixPocessor()

    def test_DetA_Zero(self):
        result = self.processor.detALaplace(np.array([[1, 1],
                                                      [2, 2]]))
        self.assertEqual(result, 0)

    def test_DetA_Double(self):
        result = self.processor.detALaplace(np.array([[1, 1],
                                                      [3, 2]]))
        self.assertEqual(result, -1)

    def test_DetA_TripleZero(self):
        result = self.processor.detALaplace(np.array([[1, 1, 1],
                                                      [2, 2, 2],
                                                      [1, 2, 3]]))
        self.assertEqual(result, 0)

    def test_DetA_Triple(self):
        result = self.processor.detALaplace(np.array([[1, 1, 1],
                                                      [2, 3, 2],
                                                      [1, 2, 3]]))
        self.assertEqual(result, 2)

    def test_DetA_Quadruple(self):
        result = self.processor.detALaplace(np.array([[1, 2, 3, 4],
                                                      [2, 3, 2, 3],
                                                      [5, 6, 3, 2],
                                                      [1, 1, 1, 1]]))
        self.assertEqual(result, -4)


class TestMinor(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.processor = MatrixPocessor()

    def test_Minor_Triple_First(self):
        result = self.processor.minor(np.array([[1, 1, 1],
                                                [2, 2, 2],
                                                [3, 3, 3]]), 0, 0)
        np.testing.assert_array_equal(result, np.array([[2, 2],
                                                        [3, 3]]))

    def test_Minor_Triple_Middle(self):
        result = self.processor.minor(np.array([[1, 1, 1],
                                                [2, 2, 2],
                                                [3, 4, 5]]), 1, 1)
        np.testing.assert_array_equal(result, np.array([[1, 1],
                                                        [3, 5]]))

    def test_Minor_Uno(self):
        result = self.processor.minor(np.array([5]), 0, 0)
        np.testing.assert_array_equal(result, np.array([5]))

class TestGaussian(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.processor = MatrixPocessor()

    def test_Gaussian_double1(self):
        result = self.processor.minor(np.array([[3.0, 2.0],
                                                [1.0, 1.0]]),
                                      np.array([5.0, 2.0]))
        np.testing.assert_array_equal(result, np.array([1, 1]))

    def test_Gaussian_double2(self):
        result = self.processor.minor(np.array([[3.0, 2.0],
                                                [2.0, 7.0]]),
                                      np.array([8, 11]))
        np.testing.assert_array_equal(result, np.array([1, 2]))

    def test_Gaussian_triple(self):
        result = self.processor.GaussianElimination(np.array([[2, 1, -1],
                                                              [-3, -1, 2],
                                                              [-2, 1, 2]], dtype=np.float32),
                                      np.array([8, -11, -3], dtype=np.float32))
        np.testing.assert_array_equal(result, np.array([2, 3, -1], dtype=np.float32))
