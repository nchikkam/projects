import unittest
from lib.fib import fibonacci

"""
    Tests for the Fibonacci method
"""
class FibonacciTest(unittest.TestCase):
    def testFibonacci(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21]
        for i in range(len(expected)):
            self.assertEqual(expected[i], fibonacci(i))

if __name__ == "__main__":
    unittest.main()