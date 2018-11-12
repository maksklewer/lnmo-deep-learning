import math
import numpy as np


class MatrixPo:

    @staticmethod
    def minor(A, i, j):
        """
        <eng>
            Calculates minor submatrix for given matrix A and given matrix position
            see: https://en.wikipedia.org/wiki/Minor_(linear_algebra)
        </eng>
        <rus>
            Вычисляет минорной матрицы для элемента исходной матрицы
            см: https://ru.wikipedia.org/wiki/Минор_(линейная_алгебра)
         </rus>
        :param A:
            <eng> input matrix <eng>
            <rus> исходная матрица <rus>
        :param i:
            <eng> column of the target element </eng>
            <rus> столбец элемента матрицы </rus>
        :param j:
            <eng> row of the target element </eng>
            <rus> строка элемента матрицы </rus>
        :return:
            <eng> Minor submatrix for element (i,j) </eng>
            <rus> Минорная матрица элемента на позиции (i,j) </rus>
        """
        return np.matrix('')

    @staticmethod
    def mult(m1, m2):
        """
        Multiplies 2 matrices
        :param m2: matrix 1
        :param m1: matrix 2
        :return: function pointer
        """
        return np.matrix('')

