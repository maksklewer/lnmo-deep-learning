import math
import numpy as np


class DemoClass:
    @staticmethod
    def demo(a, b):
        d = a + b
        return d

    @staticmethod
    def divide(a, b):
        """
        Divides 2 numbers
        :param a: number 1
        :param b: number 2
        :return: number result
        :raises TypeError: if b == 0
        """
        if b == 0:
            raise TypeError
        return a/b

