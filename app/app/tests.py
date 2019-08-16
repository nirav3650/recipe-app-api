from django.test import TestCase

from app.calc import add, subtract

class CalcTests(TestCase):


    def test_add_numbers(self):
        """Test for two numbers for adding together"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """Test that values are subtrcated and returned"""
        self.assertEqual(subtract(5, 11), -6)