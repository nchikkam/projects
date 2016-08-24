import unittest

def pairExists(arr, M):
    diff = {}
    l = len(arr)

    for i in range(l):
        t = M - arr[i]
        if (t >= 0 and t in diff):
            return 1
        diff[arr[i]] = 1
    return 0

class TestPairExistsForAGivenSum(unittest.TestCase):
    l = [10, 18, 11, 21, 28, 31, 38, 40, 55, 60, 62]
    def test_positive_case(self):
        actual = pairExists(self.l, 66)
        self.assertEqual(1, actual)

    def test_negative_case(self):
        actual = pairExists(self.l, 67)
        self.assertEqual(0, actual)

if __name__ == "__main__":
    unittest.main()