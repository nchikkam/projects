class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, spr, sbr):
    if root == None:
        root = Node(spr)
        root.left = Node(sbr)
    else:
        if root.data == spr:
            if root.left == None:
                root.left = Node(sbr)
            elif root.right == None:
                root.right = Node(sbr)
            else:
                raise ValueError("spr already manages 2 childs")
        elif root.left:
            root.left = insert(root.left, spr, sbr)
        elif root.right:
            root.right = insert(root.left, spr, sbr)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


def bfs(root):
    q = []
    q.append(root)
    while len(q) > 0:
        c = q.pop(0)
        print("{} ".format(c.data), end='')
        if c.left:
            q.append(c.left)
        if c.right:
            q.append(c.right)

def print_level(root, level):
    if root:
        if level == 0:
            print("{} ".format(root.data), end='')
        else:
            print_level(root.left, level-1)
            print_level(root.right, level - 1)

def height(root):
    if root:
        if root.left == None and root.right == None:
            return 1
        else:
            return max(height(root.left), height(root.right)) + 1
    return 0

def level_order_recursive(root):
    h = height(root)
    for i in range(h):
        print_level(root, i)
        print()

data = [
    ("1", "2"),
    ("1", "3"),
    ("2", "4"),
    ("4", "5"),
    ("4", "6"),
]

root = None
spr = None
for spr, sbr in data:
    root = insert(root, spr, sbr)

#inorder(root)
level_order_recursive(root)
