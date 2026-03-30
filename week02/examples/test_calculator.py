import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)

    def test_add_floats(self):
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtract_negative_result(self):
        self.assertEqual(self.calc.subtract(3, 10), -7)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(999, 0), 0)

    def test_multiply_negatives(self):
        self.assertEqual(self.calc.multiply(-3, -4), 12)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)

    def test_divide_by_zero_raises_error(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_divide_returns_float(self):
        result = self.calc.divide(7, 2)
        self.assertIsInstance(result, float)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 10), 1024)

    def test_power_zero_exponent(self):
        self.assertEqual(self.calc.power(99, 0), 1)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_by_zero_raises_error(self):
        with self.assertRaises(ValueError):
            self.calc.modulo(10, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)