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

def inorder(root):
    if root != None:
        inorder(root.left)
        print("{} ".format(root.data), end='')
        inorder(root.right)

def preorder(root):
    if root != None:
        print("{} ".format(root.data), end='')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root != None:
        postorder(root.left)
        postorder(root.right)
        print("{} ".format(root.data), end='')

def dfs(root):
    inorder(root)  # this uses implicit stack

def bfs(root):
    q = [root]
    while len(q) != 0:
        current = q.pop(0)
        print( current.data)
        if current.left != None:
            q.append(current.left)
        if current.right != None:
            q.append(current.right)

def bfs_spiral_order(root):
    """
        +------------< 11 <------------< START
        +-----> 6               19 >------------------+
    +------<4       8       17        43   <----------+
    +--->3     5   7  10   16   18   31   49 ->END

    """
    pq = [root]
    cq = []
    print(root.data)
    flag=-1
    while len(pq) != 0:
        current = pq.pop(0)
        if current.left != None:
            cq.append(current.left)
        if current.right != None:
            cq.append(current.right)
        if len(pq) == 0:
            flag *= -1  # flip the direction
            pq = cq[:]  # copy to parent queue
            cq = []
            toprint = [str(x.data) for x in pq]

            if flag==1:
                print("".join(toprint))
            else:
                print("".join(reversed(toprint)))

def count_leaves(root):
    if root:
        if root.left == None and root.right == None:
            return 1
        return count_leaves(root.left) + count_leaves(root.right)
    return 0

def count_internal_nodes(root):
    if root:
        if root.left == None and root.right == None:
            return 0
        return count_internal_nodes(root.left) + count_internal_nodes(root.right) + 1
    return 0

def count_nodes(root):
    if root:
        return count_nodes(root.left)+count_nodes(root.right)+1
    return 0

def find_nth_smallest(root, n):
    if root:
        l = find_nth_smallest(root.left, n)
        lc = count_nodes(root.left)
        if lc + 1 == n: return root

        rc = count_nodes(root.right)
        c = n
        if lc + rc + 1 >= n:
            c = n - (lc+1)
        r = find_nth_smallest(root.right, c)

        if l: return l
        return r

def find_nth_biggest(root, n):
    if root:
        r = find_nth_biggest(root.right, n)
        rc = count_nodes(root.right)
        if rc + 1 == n: return root

        lc = count_nodes(root.left)
        c = n
        if rc + lc + 1 >= n:
            c = n - (rc+1)
        l = find_nth_biggest(root.left, c)

        if r: return r
        return l

def height(root):
    if root:
        return max(
            height(root.left), \
            height(root.right)
        ) + 1
    return 0

def max_width(root): # same as bfs spiral order
    pq = [root]
    cq = []
    wid = 1
    while len(pq) != 0:
        current = pq.pop(0)
        if current.left != None:
            cq.append(current.left)
        if current.right != None:
            cq.append(current.right)
        if len(pq) == 0:
            pq = cq[:]  # copy to parent queue
            cq = []
            if wid < len(pq):
                wid = len(pq)
    return wid

def to_doubly_linked_list(root):
    def convert_to_list(root):
        if root:
            # find inorder predecessor of root
            if root.left:
                l = convert_to_list(root.left)
                while l.right:
                    l = l.right
                l.right = root
                root.left = l

            # find inorder successor of root
            if root.right:
                r = convert_to_list(root.right)
                while r.left:
                    r = r.left
                r.left = root
                root.right = r
            return root
        return None

    head = convert_to_list(root)
    # move to head
    while head.left:
        head = head.left

    return head

def print_dll(dll):
    while dll:
        print("{} ".format(dll.data), end='')
        dll = dll.right

def find_min(root):
    while root.left:
        root = root.left
    return root

def delete(root, data):
    if root:
        if data < root.data:
            root.left = delete(root.left, data)
        elif data > root.data:
            root.right = delete(root.right, data)
        elif root.left and root.right:
            l = find_min(root.right)
            root.data = l.data
            root.right = delete(root.right, l.data)
        elif root.left == None and root.right == None:
            return None
        else:
            if root.left:
                root = root.left
            elif root.right:
                root = root.right
        return root
    return None

def search(root, x):
    if root:
        if x < root.data:
            return search(root.left, x)
        elif x > root.data:
            return search(root.right, x)
        else:
            return True
    return False

def inorder_successor(root, x):
    succ = None
    while root:
        if x < root.data:
            succ = root
            root = root.left
        else:
            root = root.right
    return succ

def inorder_predecessor(root, x):
    pred = None
    while root:
        if x > root.data:
            pred = root
            root = root.right
        else:
            root = root.left
    return pred

def preorder_sccessor(root, data, d):
   if root:
       if data==root.data:
           d['found'] = True
           if root.left:
               return root.left
           else:
               return root.right

       succs = preorder_sccessor(root.left, data, d)
       if succs==None:
           if d['found']:
               return root.right
           else:
               return preorder_sccessor(root.right, data, d)
       else:
           return succs
   return None

def find_left_most(root):
    while root and root.left:
        root = root.left
    return root

def find_right_most(root):
    while root and root.right:
        root = root.right
    return root

def preorder_predecessor(root, data, d):
    def preorder_predecessor_parent(root, parent, data, d):
        if root:
            if data == root.data:
                d['found'] = True
                return parent

            preds = preorder_predecessor_parent(root.left, root, data, d)
            if preds == None:
                if d['found']:
                    return parent
                else:
                    preds = find_right_most(root.left)
                    return preorder_predecessor_parent(root.right, preds, data, d)
            else:
                return preds
        return None

    return preorder_predecessor_parent(root, None, data, d)

def lowest_common_ancestor_bst(root, a, b):  # good because if searches for key presence
    if root:
        if root.data == a or root.data == b:
            return root
        elif search(root.left, a) and search(root.right, b):
            return root
        elif search(root.left, a): #lca in left subtree
            return lowest_common_ancestor_bst(root.left, a, b)
        else:
            return lowest_common_ancestor_bst(root.right, a, b)

def lowest_common_ancestor(root, a, b):
    if root:
        if root.data == a or root.data == b:
            return root
        l = lowest_common_ancestor(root.left, a, b)
        r = lowest_common_ancestor(root.right, a, b)
        if l and r:
            return root
        if l:
            return l
        if r:
            return r

    return None

def find_path(root, a, b):
    def find_path_from_lca(root, a, b, path):
        if root:
            if root.data == a or root.data == b:
                path.append(root)
                return True

            l = find_path_from_lca(root.left, a, b, path)
            r = find_path_from_lca(root.right, a, b, path)

            if l:
                path.append(root)
                return True
            elif r:
                path.append(root)
                return True
            else:
                return False
        return False

    lca = lowest_common_ancestor(root, a, b)
    path_one = []
    path_two = []
    find_path_from_lca(lca.left, a, b, path_one)
    find_path_from_lca(lca.right, a, b, path_two)
    return path_one + [lca] + list(reversed(path_two))

def get_right_node_using_preorder(node):  # node is not root and has parent pointer

    """Idea:
        Have a count = 0 when we find that element
        increment count while going up the tree levels
        decrementing it while going down, first time when
        we see count == 0 we found the first element
    """
    def find_right(root, node, d):
        if root:
            if 'count' in d and d['count'] == 0:
                print(root.data)
                return root

            if root.data == node.data:
                d['count'] = 0 # start counter

            if 'count' in d:
                d['count'] -= 1
            find_right(root.left, node, d)
            find_right(root.right, node, d)

            if 'count' in d:
                d['count'] += 1

    root = node
    while root.parent != None:
        root = root.parent
    d = {}
    return find_right(root, node, d)

def get_right_node_using_bfs(node):  # node is not root and has parent pointer
    root = node
    while root.parent != None:
        root = root.parent

    q = []
    b = []
    q.append(root)
    while len(q) > 0:
        c = q.pop(0)
        if c.data == node.data:
            if len(q) > 0:
                return q[0].data
            return None

        if c.left: b.append(c.left)
        if c.right: b.append(c.right)

        if len(q) == 0:
            q = b[:]
            b = []

def test():
    root = None
    data = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49]
    for d in data:
        root = insert(root, d)

    print(count_internal_nodes(root))

    #bfs_spiral_order(root)
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    print(count_leaves(root))

def test_one():
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

    print(count_internal_nodes(root))


def test_two():
    root = None
    data = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49]
    for d in data:
        root = insert(root, d)
    print(count_nodes(root))

def test_three():
    root = None
    wdata = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49]
    data = [4, 2, 6, 1, 3, 5, 7]
    for d in data:
        root = insert(root, d)

    data.sort()
    for i, n in enumerate(data):
        print("{} ".format(find_nth_smallest(root, i+1).data), end='')

    print("\n")

    i = len(data)
    while i > 0:
        print("{} ".format(find_nth_biggest(root, i).data), end='')
        i -= 1
    print("\n")
    print (height(root))

    print("\n")
    print(max_width(root))

def test_four():
    data = [4, 2, 6, 1, 3, 5, 7]
    root = None
    for d in data:
        root = insert(root, d)

    print("\n")
    dll = to_doubly_linked_list(root)
    print_dll(dll)

    data = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49]
    root = None
    for d in data:
        root = insert(root, d)

    print("\n")
    dll = to_doubly_linked_list(root)
    print_dll(dll)

def test_five():
    data = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49]
    root = None
    for d in data:
        root = insert(root, d)

    print("\n")
    print(find_min(root).data)

    d = [3, 4, 5, 6, 7, 8, 10, 11, 16, 17, 18, 19, 31, 43, 49]
    for v in d:
        root = delete(root, v)
        inorder(root)
        print("\n")

def test_six():
    data = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49]
    root = None
    for d in data:
        root = insert(root, d)
    for d in data:
        print(search(root, d))

    print(search(root, 100))

def test_seven():
    data = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49]
    root = None
    for d in data:
        root = insert(root, d)

    print(inorder_successor(root, 16).data)
    print(inorder_successor(root, 31).data)
    print(inorder_successor(root, 18).data)
    print(inorder_successor(root, 10).data)
    print(inorder_successor(root, 19).data)


    print(inorder_predecessor(root, 16).data)
    print(inorder_predecessor(root, 11).data)
    print(inorder_predecessor(root, 19).data)
    print(inorder_predecessor(root, 4).data)


def test_eight():
    data = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49]
    root = None
    for d in data:
        root = insert(root, d)

    preorder(root) # 11 6 4 3 5 8 7 10 19 17 16 18 43 31 49
    print("\n")
    print(preorder_sccessor(root, 4, {'found': False}).data)
    print(preorder_sccessor(root, 5, {'found': False}).data)
    print(preorder_sccessor(root, 19, {'found': False}).data)
    print(preorder_sccessor(root, 31, {'found': False}).data)
    print(preorder_sccessor(root, 43, {'found': False}).data)

def test_nine():
    data = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49]
    root = None
    for d in data:
        root = insert(root, d)

    preorder(root) # 11 6 4 3 5 8 7 10 19 17 16 18 43 31 49
    print("\n")
    print(preorder_predecessor(root, 4, {'found': False}).data)
    print(preorder_predecessor(root, 6, {'found': False}).data)
    print(preorder_predecessor(root, 49, {'found': False}).data)
    print(preorder_predecessor(root, 31, {'found': False}).data)
    print(preorder_predecessor(root, 43, {'found': False}).data)
    print(preorder_predecessor(root, 18, {'found': False}).data)
    print(preorder_predecessor(root, 16, {'found': False}).data)
    print(preorder_predecessor(root, 17, {'found': False}).data)
    print(preorder_predecessor(root, 19, {'found': False}).data)
    print(preorder_predecessor(root, 10, {'found': False}).data)
    print(preorder_predecessor(root, 7, {'found': False}).data)
    print(preorder_predecessor(root, 8, {'found': False}).data)
    print(preorder_predecessor(root, 5, {'found': False}).data)
    print(preorder_predecessor(root, 3, {'found': False}).data)

def test_ten():
    d = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49]
    root = None
    for v in d:
        root = insert(root, v)

    lca = lowest_common_ancestor(root, 19, 19)
    print(lca.data)
    lca = lowest_common_ancestor(root, 19, 49)
    print(lca.data)
    lca = lowest_common_ancestor(root, 17, 49)
    print(lca.data)
    lca = lowest_common_ancestor(root, 16, 16)
    print(lca.data)
    lca = lowest_common_ancestor(root, 16, 18)
    print(lca.data)
    lca = lowest_common_ancestor(root, 5, 18)
    print(lca.data)
    lca = lowest_common_ancestor(root, 18, 5)
    print(lca.data)
    lca = lowest_common_ancestor(root, 49, 31)
    print(lca.data)
    lca = lowest_common_ancestor(root, 49, 16)
    print(lca.data)
    lca = lowest_common_ancestor(root, 49, 18)
    print(lca.data)
    lca = lowest_common_ancestor(root, 18, 10)
    print(lca.data)
    lca = lowest_common_ancestor(root, 10, 18)
    print(lca.data)


def test_11():
    data = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49]
    root = None
    for d in data:
        root = insert(root, d)

    path = find_path(root, 16, 49)
    print([x.data for x in path])

    path = find_path(root, 10, 49)
    print([x.data for x in path])

    path = find_path(root, 10, 31)
    print([x.data for x in path])

    path = find_path(root, 31, 5)
    print([x.data for x in path])

    path = find_path(root, 18, 5)
    print([x.data for x in path])

    path = find_path(root,3, 3)
    print([x.data for x in path])

    path = find_path(root, 10, 16)
    print([x.data for x in path])

    path = find_path(root, 8, 43)
    print([x.data for x in path])


def test_12():
    class Node:
        def __init__(self, data, parent):
            self.data = data
            self.left = None
            self.right = None
            self.parent = parent

    root = (4, (2, (1), (3)), (6, (5), (7)))

    root = Node(4, None)
    root.left = Node(2, root)
    root.right = Node(6, root)

    root.left.left = Node(1, root.left)
    root.left.right = Node(3, root.left)

    root.right.left = Node(5, root.right)
    root.right.right = Node(7, root.right)

    x = root
    print(get_right_node_using_preorder(x))
    print(get_right_node_using_bfs(x))

test_12()