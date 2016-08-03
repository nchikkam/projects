import unittest
from lib.fizzbuzz import fizzbuzz
from lib.prime import is_prime

"""
    Test to verify fizzbuzz functionality alone.
"""
class FizzBuzzTest(unittest.TestCase):
    def testFizz(self):
        self.assertEqual("Fizz", fizzbuzz(5))

    def testBuzz(self):
        self.assertEqual("Buzz", fizzbuzz(3))

    def testFizzBuzz(self):
        self.assertEqual("FizzBuzz", fizzbuzz(0))
        self.assertEqual("FizzBuzz", fizzbuzz(15))

    def testBuzzFizz(self):
        self.assertEqual("BuzzFizz", fizzbuzz(2))

    def testBuzzFizzForPrimesRegression(self):
        for i in range(4, 100):
            if is_prime(i) and i != 3 and i != 5:
                self.assertEqual("BuzzFizz", fizzbuzz(i))

if __name__ == "__main__":
    unittest.main()