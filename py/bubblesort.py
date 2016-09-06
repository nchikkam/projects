def bubbleSort(arr):
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            if arr[i] >= arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

import unittest
import random

class BubbleSortTest(unittest.TestCase):

    def generateTestData(self):
        data = []
        for i in range(15):
            data.append(random.randrange(100))
        return data

    def testBubbleSort(self):
        data = self.generateTestData()
        original = data[:]
        print(original)
        bubbleSort(data)
        print(data)
        for i in range(1, len(data)):
            self.assertTrue(data[i-1] <= data[i])

if __name__ == "__main__":
    unittest.main()