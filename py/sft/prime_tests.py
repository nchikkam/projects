import unittest
from lib.prime import is_prime

"""
    Tests for the PrimeNumber method
"""
class PrimeNumberTest(unittest.TestCase):
    def testPrimeOrNot(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        i = 0
        for j in range(2, 24):
            if is_prime(j):
                self.assertEqual(primes[i], j)
                i += 1
                #print "{0} is prime".format(j)

if __name__ == "__main__":
    unittest.main()