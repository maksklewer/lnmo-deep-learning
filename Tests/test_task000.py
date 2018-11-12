from unittest import TestCase
from Tasks.Task000 import DemoClass


class TestDemoClass(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calculator = DemoClass()

    def test_demo(self):
        res = self.calculator.demo(1, 2)
        self.assertEqual(res, 3)

    def test_divide_normal(self):
        res = self.calculator.divide(4, 2)
        self.assertEqual(res, 2)

    def test_divide_error(self):
        with self.assertRaises(TypeError):
            self.calculator.divide("abbb", "bbbb")