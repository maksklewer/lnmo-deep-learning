import math
import numpy as np


class MatrixPocessor:

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
    def detALaplace(A):
        """
        <eng>
            Calculates determinant for given matrix A, using Laplace row/column expansion method.
            https://en.wikipedia.org/wiki/Laplace_expansion
            https://en.wikipedia.org/wiki/Determinant#Laplace's_formula_and_the_adjugate_matrix
        </eng>
        <rus>
            Вычисляет определитель данной матрицы A, используя Метод разложения по строке/столбцу Лапласа.
            см: https://ru.wikipedia.org/wiki/Теорема_Лапласа
                https://ru.wikipedia.org/wiki/Определитель
         </rus>
        :param A:
            <eng> input matrix <eng>
            <rus> исходная матрица <rus>
        :return:
            <eng> Matrix Determinant </eng>
            <rus> Определитель матрицы </rus>
        """
        return ''

    @staticmethod
    def GaussianElimination(A,b):
        """
        <eng>
            Solves system linear equation given in matrix form using Gaussian elimination method

            https://en.wikipedia.org/wiki/Gaussian_elimination
            Example:
                If we have such SLE:
                    |3*x1+1*x2 = 10
                    |2*x1+3*x2 = 16
                The input will be following:
                    Matrix A : [[ 3 , 1 ],
                                 [ 2 , 3 ]]
                    Vector b : [ 10 , 16
                Output:
                    Vector: [2, 4]
            https://en.wikipedia.org/wiki/Gaussian_elimination
            http://matrixcalc.org/slu.html

        </eng>
        <rus>
            Решает систему линейных уравнений используя метод Гаусса.
            Пример:
                Если дана система уравнений:
                    |3*x1+1*x2 = 10
                    |2*x1+3*x2 = 16
                То входными данными будут:
                    Матрица A : [[ 3 , 1 ],
                                 [ 2 , 3 ]]
                    Вектор b : [ 10 , 16
                Результат работы программы:
                    Вектор : [2, 4]
            https://ru.wikipedia.org/wiki/Метод_Гаусса
            http://matrixcalc.org/slu.html
         </rus>
        :param A:
            <eng> input matrix <eng>
            <rus> исходная матрица <rus>
        :param b:
            <eng> vector of free coefficients<eng>
            <rus> свободные коэффициенты <rus>
        :return:
            <eng> solution vector  x1,...xn </eng>
            <rus> вектор-решение СЛОУ x1,...,xn </rus>
        """
        return np.array('')
