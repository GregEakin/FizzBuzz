import unittest

from main import print_num


class TestSum(unittest.TestCase):
    def test_one(self):
        number = print_num(1)
        self.assertEqual("1", number)

    def test_two(self):
        number = print_num(2)
        self.assertEqual("2", number)

    def test_three(self):
        number = print_num(3)
        self.assertEqual("Fizz", number)

    def test_five(self):
        number = print_num(5)
        self.assertEqual("Buzz", number)

    def test_fifteen(self):
        number = print_num(15)
        self.assertEqual("FizzBuzz", number)
