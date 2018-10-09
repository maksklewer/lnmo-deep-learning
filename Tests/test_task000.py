from unittest import TestCase
from Tasks.Task000 import DemoClass


class TestDemoClass(TestCase):
    def test_demo(self):
        calculator = DemoClass()
        res = calculator.demo(1, 2)
        self.assertEqual(res, 3)

    def test_divide_normal(self):
        calculator = DemoClass()
        res = calculator.divide(4, 2)
        self.assertEqual(res, 2)

    def test_divide_error(self):
        calculator = DemoClass()
        with self.assertRaises(TypeError):
            calculator.divide(4,0)


