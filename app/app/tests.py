"""
SAMPLE TEST
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """
    TEST CALC MODULE
    """

    def test_add_numbers(self):
        """
        Test adding number together.
        :return:
        """

        res = calc.add(a=5, b=10)

        self.assertEqual(res, 15)

    def test_subtract_numbers(self):
        """
        Test subtracting numbers.
        :return:
        """

        res = calc.subtract(a=10, b=1)

        self.assertEqual(res, 9)
