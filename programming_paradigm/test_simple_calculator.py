import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a new SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # ------------------ Addition Tests ------------------
    def test_addition(self):
        """Test the addition method with positive, negative, and zero values."""
        self.assertEqual(self.calc.add(2, 3), 5)          # positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)         # negative + positive
        self.assertEqual(self.calc.add(-5, -5), -10)      # negative numbers
        self.assertEqual(self.calc.add(0, 10), 10)        # adding zero

    # ------------------ Subtraction Tests ------------------
    def test_subtraction(self):
        """Test the subtraction method with various cases."""
        self.assertEqual(self.calc.subtract(10, 5), 5)    # normal case
        self.assertEqual(self.calc.subtract(0, 5), -5)    # subtract from zero
        self.assertEqual(self.calc.subtract(-5, -5), 0)   # negatives
        self.assertEqual(self.calc.subtract(5, 10), -5)   # result negative

    # ------------------ Multiplication Tests ------------------
    def test_multiplication(self):
        """Test the multiplication method with different numbers."""
        self.assertEqual(self.calc.multiply(4, 5), 20)    # positives
        self.assertEqual(self.calc.multiply(-2, 3), -6)   # negative * positive
        self.assertEqual(self.calc.multiply(-3, -3), 9)   # negative * negative
        self.assertEqual(self.calc.multiply(0, 100), 0)   # multiply by zero

    # ------------------ Division Tests ------------------
    def test_division(self):
        """Test the division method with normal inputs and edge cases."""
        self.assertEqual(self.calc.divide(10, 2), 5)      # normal case
        self.assertEqual(self.calc.divide(-9, 3), -3)     # negative result
        self.assertEqual(self.calc.divide(5, 2), 2.5)     # float result
        self.assertEqual(self.calc.divide(0, 5), 0)       # zero numerator
        self.assertIsNone(self.calc.divide(10, 0))        # division by zero


if __name__ == "__main__":
    unittest.main()
