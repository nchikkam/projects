import unittest
import random

def binSearchRecursive(arr, low, high, element):
    mid = (low+high)//2
    if element == arr[mid]:
        return mid
    elif element > arr[mid]:
        low = mid + 1
    else:
        high = mid -1
    return binSearchRecursive(arr, low, high, element)

def binSearch(arr, low, high, element):

    while low <= high:
        mid = (low + high) >> 1

        if element < arr[mid]:
            high = mid -1
        elif element > arr[mid]:
            low = mid +1
        else:
            return mid
    return -1


class BinSearchTest(unittest.TestCase):

    def testBinarySearch(self):
        data = list(range(10))
        self.assertTrue(binSearch(data, 0, len(data), 7) != -1)

    def testBinSearch(self):
        size = 10
        arr = random.sample(list(range(1, 20)), size)
        elem = arr[0]
        arr.sort()
        self.assertTrue(binSearch(arr, 0, len(arr), elem) != -1)

if __name__ == "__main__":
    unittest.main()