def solution(T):

    def get_left_depth(N):  # O(log N)
        """just finds out the left height"""
        if N:
            if N.l:
                l = get_left_depth(N.l)
                return l + 1
            return 0
        return 0

    def get_right_depth(N):   # O(log N)
        """just finds out the right height"""
        if N:
            if N.r:
                r = get_right_depth(N.r)
                return r + 1
            return 0
        return 0

    lengths = {}  # container to store the path lengths

    # standard bfs algorithm O(N)
    def bfsTraversal(N):
        q = []  # queue to store the nodes in BFS Order
        index = 0
        if N.l == None and N.r == None:
            return
        q.append(N)
        while len(q) > 0:
            current = q.pop(0)
            lengths[index] = max(get_left_depth(current.l), get_right_depth(current.r)) + 1
            index += 1
            if current.l:
                q.append(current.l)
            if current.r:
                q.append(current.r)

    bfsTraversal(T)
    sol = -1
    for k in lengths:   # O(N)
        if sol < int(lengths[k]):
            sol = int(lengths[k])

    return sol

class Tree(object):
    x = 0
    l = None
    r = None

import unittest
class TreeMaxLengthPathTest(unittest.TestCase):
    def test_case_one(self):
        # (5, (3, None, None), (10, (12, (21, None, None), (20, None, None)), None))
        # note, either the path goes only left or right.
        root = Tree()
        root.l = Tree()
        root.r = Tree()
        root.r.l = Tree()
        root.r.l.l = Tree()
        root.r.l.r = Tree()
        #print(solution(root))
        self.assertEqual(2, solution(root))

    def test_case_two(self):
        #(5, (4, (3, (2, (1, None, None), None), None), None), None)
        root = Tree()               #5
        root.l = Tree()             #4
        root.l.l = Tree()           #3
        root.l.l.l = Tree()         #2
        root.l.l.l.l = Tree()       #1
        #print(solution(root))
        self.assertEqual(4, solution(root))

if __name__ == "__main__":
    unittest.main()