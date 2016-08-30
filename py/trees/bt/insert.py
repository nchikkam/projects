class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def insert(root, data):
    if root == None:
        return Node(data)
    if  data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    #we dont insert duplicates
    return root

import unittest
class Test(unittest.TestCase):
    def test_insert(self):
        """
                    4
            2               6
        1       3       5        7
        """
        root = None
        root = insert(root, 4)
        root = insert(root, 2)
        root = insert(root, 6)
        root = insert(root, 1)
        root = insert(root, 3)
        root = insert(root, 5)
        root = insert(root, 7)

        self.assertEquals(root.data, 4)
        self.assertEquals(root.left.data, 2)
        self.assertEquals(root.left.left.data, 1)
        self.assertEquals(root.left.right.data, 3)
        self.assertEquals(root.right.data, 6)
        self.assertEquals(root.right.left.data, 5)
        self.assertEquals(root.right.right.data, 7)

        # leaf nodes
        self.assertEquals(root.left.left.left, None)
        self.assertEquals(root.left.left.right, None)
        self.assertEquals(root.left.right.left, None)
        self.assertEquals(root.left.right.right, None)

        self.assertEquals(root.right.left.left, None)
        self.assertEquals(root.right.left.right, None)
        self.assertEquals(root.right.right.left, None)
        self.assertEquals(root.right.right.right, None)

if __name__ == "__main__":
    unittest.main()