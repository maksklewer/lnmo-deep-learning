import math
import numpy as np


class MatrixCalculator:
    @staticmethod
    def demo(a, b, c):

        d = b ** 2 - 4 * a * c

        if d >= 0:
            disc = math.sqrt(d)
            root1 = (-b + disc) / (2 * a)
            root2 = (-b - disc) / (2 * a)
            print(root1, root2)
        else:
            raise Exception

    @staticmethod
    def sum(m1, m2):
        """
        Calculates sum of 2 matrices
        :param m2: matrix 1
        :param m1: matrix 2
        :return: function pointer
        """
        return np.matrix('2 2;4 4')

    @staticmethod
    def mult(m1, m2):
        """
        Multiplies 2 matrices
        :param m2: matrix 1
        :param m1: matrix 2
        :return: function pointer
        """
        return np.matrix('')


MatrixCalculator().demo(2, 1, 0)
