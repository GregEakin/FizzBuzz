# This is a sample Python script.

class Number:
    def print(self, number):
        return f'{number}'


class Fizz:
    def print(self, number):
        return "Fizz"


class Buzz:
    def print(self, number):
        return "Buzz"


class FizzBuzz:
    def print(self, number):
        return "FizzBuzz"


def print_num(number):
    lst = [FizzBuzz, Number, Number, Fizz, Number, Buzz, Fizz, Number, Number, Fizz, Buzz, Number, Fizz, Number, Number]
    index = number % 15
    return lst[index]().print(number)
