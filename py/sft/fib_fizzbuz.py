from lib.fib import fibonacci
from lib.fizzbuzz import fizzbuzz
import argparse
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


"""
    This is the main driver method to print the sequence required:
    Sample run:
    C:\Python27\python.exe fib_fizzbuz.py --number 9
    FizzBuzz
    1
    1
    BuzzFizz
    Buzz
    Fizz
    8
    BuzzFizz
    Buzz
    34
"""
def fib_fizzbuzz(n):
    for i in range(n):
        n = fibonacci(i)
        print fizzbuzz(n)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='fibonacci based fizzbuzz method'
    )

    parser.add_argument(
        '--number',
        help='an integer to generate fizz, buzz, fizzbuzz, buzzfizz, number sequence for fibonacci(i) for every i <= number'
    )
    args = parser.parse_args()

if args.number:
    number = int(args.number)
    fib_fizzbuzz(number)
else:
    logging.info("Please pass all the positional Arguments and try again.")