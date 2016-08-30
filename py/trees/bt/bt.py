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
        print(root.data, end='')
        inorder(root.right)

def preorder(root):
    if root != None:
        print(root.data, end='')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root != None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end='')

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



def test():
    root = None
    data = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49]
    for d in data:
        root = insert(root, d)

    #bfs_spiral_order(root)
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    print(count_leaves(root))


test()