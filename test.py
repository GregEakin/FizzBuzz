import unittest

from main import print_fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    def test_one(self):
        number = print_fizz_buzz(1)
        self.assertEqual("1", number)

    def test_two(self):
        number = print_fizz_buzz(2)
        self.assertEqual("2", number)

    def test_three(self):
        number = print_fizz_buzz(3)
        self.assertEqual("Fizz", number)

    def test_five(self):
        number = print_fizz_buzz(5)
        self.assertEqual("Buzz", number)

    def test_fifteen(self):
        number = print_fizz_buzz(15)
        self.assertEqual("FizzBuzz", number)

    def test_sixteen(self):
        number = print_fizz_buzz(16)
        self.assertEqual("16", number)

    def test_first_fifty(self):
        for i in range(1, 51):
            print(f'{i:2}    { print_fizz_buzz(i)}')
