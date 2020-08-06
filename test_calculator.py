import unittest
from calculator import addition, subtraction, multiplication, division
class TestCalculator(unittest.TestCase):
    def  test_addition(self):
        result = addition(50, 25)
        self.assertEqual(result, 75)

    def  test_subtraction(self):
        result = subtraction(50, 25)
        self.assertEqual(result, 25)

    def  test_multiplication(self):
        result = multiplication(50, 2)
        self.assertEqual(result, 100)

    def  test_division(self):
        result = division(50, 25)
        self.assertEqual(result, 2)
