class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def nth_node_using_n_space(root, n):
    ret = []
    def inorder(root):
        if root != None:
            inorder(root.left)
            ret.append(root)
            inorder(root.right)

    inorder(root)
    return ret[n-1]

def nth_node_using_global_count(root, n):
    x = {"count": 0}  # using a variable instead reports error in python
    def inorder(root):
        if root != None:
            l = inorder(root.left)
            x["count"] += 1
            if x["count"] == n:
                return root
            r = inorder(root.right)
            if l: return l
            return r

    return inorder(root)

def nth_node_using_count_helper(root, n):
    def count(root):
        if root:
            return count(root.left) + count(root.right) + 1
        else:
            return 0
    if root!=None:
        l = nth_node_using_count_helper(root.left, n)
        lc = count(root.left)
        if lc+1 == n: return root

        rest = n
        rc = count(root.right)
        if (lc + rc + 1) >= n:
            rest =  n-(lc+1)
        r = nth_node_using_count_helper(root.right, rest)

        if l: return l
        return r

def nth_node(root, x, n): # same as using global variable, but as argument
    if root != None:
        l = nth_node(root.left, x, n)
        x["count"] += 1
        if x["count"] == n:
            return root
        r = nth_node(root.right, x, n)
        if l: return l
        return r


import unittest

class NthNodeInBinaryTree(unittest.TestCase):
    """
                    8
            2
        1       4
            3      5
    """
    root = Node(8)
    root.left = Node(2)
    root.left.left = Node(1)

    root.left.right = Node(4)
    root.left.right.left = Node(3)
    root.left.right.right = Node(5)

    expected = [1, 2, 3, 4, 5, 8]

    def test_nth_node(self):
        for i, n in enumerate(self.expected):
            x = {'count': 0}
            self.assertEquals(
                n,
                nth_node(self.root, x, i+1).data
            )

    def test_nth_node_using_count_helper(self):
        for i, n in enumerate(self.expected):
            self.assertEquals(
                n,
                nth_node_using_count_helper(self.root, i + 1).data
            )

    def test_nth_node_using_global_count(self):
        for i, n in enumerate(self.expected):
            self.assertEquals(
                n,
                nth_node_using_global_count(self.root, i + 1).data
            )

    def test_nth_node_using_n_space(self):
        for i, n in enumerate(self.expected):
            self.assertEquals(
                n,
                nth_node_using_n_space(self.root, i + 1).data
            )

if __name__ == "__main__":
    unittest.main()