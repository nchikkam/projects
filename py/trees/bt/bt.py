class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class CNode:  # Custom node definition
    def __init__(self, data):
        self.data = data
        self.left = self.right = self.next = None


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
        print("{} ".format(current.data), end='')
        if current.left != None:
            q.append(current.left)
        if current.right != None:
            q.append(current.right)

def bfs_recursion(root):
    h = height(root)
    for i in list(range(h+1)):
        print_nodes_at_level(root, i)
        print("\n")


def bfs_spiral_order_using_queues(root):
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
                print(" ".join(toprint))
            else:
                print(" ".join(reversed(toprint)))

def print_spiral_order_using_stacks(root):
    stk_one = []
    stk_two = []
    stk_one.append(root)
    while len(stk_one) > 0 or len(stk_two) > 0:
        print("\n")
        while len(stk_one) > 0:
            c = stk_one.pop()
            print("{} ".format(c.data), end='')
            if c.right:
                stk_two.append(c.right)
            if c.left:
                stk_two.append(c.left)
        print("\n")
        while len(stk_two) > 0:
            c = stk_two.pop()
            print("{} ".format(c.data), end='')
            if c.left:
                stk_one.append(c.left)
            if c.right:
                stk_one.append(c.right)

def print_spiral_order_using_recursion(root):

    def print_level(root, level, flag):
        if root == None:
            return
        if level == 1:
            print("{} ".format(root.data), end='')
        else:
            if flag:  # left to right
                print_level(root.left, level-1, flag)
                print_level(root.right, level - 1, flag)
            else:     # right to left
                print_level(root.right, level - 1, flag)
                print_level(root.left, level - 1, flag)

    h = height(root)
    flag = True
    for i in list(range(h+1)):
        print_level(root, i, flag)
        flag = not flag
        print("\n")


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

def to_doubly_linked_list_sol2(root):
    if root:
        l = to_doubly_linked_list_sol2(root.left)
        r = to_doubly_linked_list_sol2(root.right)

        if l == None and r == None:
            return root

        if l != None:
            t = l
            while t.right:
                t = t.right
            t.right = root
            root.left =t

        if r != None:
            t = r
            while t.left:
                t = t.left
            t.left = root
            root.right = t

        while root.left:
            root = root.left
        return root

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

def inorder_predecessor_bt(root, x):
    if root == None: return None
    if root.data == x:
        if root.left:
            return find_right_most(root.left)
        return None

    l = inorder_predecessor_bt(root.left, x)
    if l: return l
    # check if x is left most in root's right
    if root.right:
        h = find_left_most(root.right)
        if h.data == x:
            return root
        else:
            return inorder_predecessor_bt(root.right, x)
    else:
        return None

def inorder_successor_bt(root, x):
    if root == None: return None
    if root.data == x:
        if root.right:
            return find_left_most(root.right)
        return None

    r = inorder_successor_bt(root.right, x)
    if r:
        return r

    # check if x is right most in root's left
    if root.left:
        h = find_right_most(root.left)
        if h.data == x:
            return root
        else:
            return inorder_successor_bt(root.left, x)
    else:
        return None





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

def get_range(root, start, end): # works for both BT & BST
    if root:
        get_range(root.left, start, end)
        if root.data >= start and root.data <= end:
            print("{} ".format(root.data), end='')
        get_range(root.right, start, end)


def print_nodes_at_level(root, level):
    if root:
        if level == 1:
            print("{} ".format(root.data), end='')

        print_nodes_at_level(root.left, level-1)
        print_nodes_at_level(root.right, level-1)

def print_braces_format(root):
    if root:
        if root.left == None and root.right == None:
            print("{},".format(root.data), end='')
            return
        print("({},".format(root.data), end='')
        print_braces_format(root.left)
        print_braces_format(root.right)
        print("),", end='')

def get_parenthesis_representation(root):
    if root:
        r = [root.data]
        if root.left == None and root.right == None:
            return root.data
        r.append(get_parenthesis_representation(root.left))
        r.append(get_parenthesis_representation(root.right))
        return tuple(r)

def create_from_parenthesis(fmt):
    if fmt:
        if type(fmt) is tuple:
            r = CNode(fmt[0])
            r.left = create_from_parenthesis(fmt[1])
            r.right = create_from_parenthesis(fmt[2])
            return r
        else:
            return CNode(fmt)

def print_level_order_using_pointers(root):
    # Careful this expects a next pointer in each Node
    # look for CNode's Definition in this file
    nxt = root
    d = None
    while nxt:
        while nxt:
            print("{} ".format(nxt.data), end='')
            if d == None:
                if nxt.left:
                    d = nxt.left  # next level head
                else:
                    d = nxt.right
            nxt = nxt.next
        nxt = d
        d = None



def connect_tree_non_recursive(root):
    while root:
        head = None
        while root:
            if root.left:
                if head == None: head = root.left  # bfs strategy to just hold the first link 'head' in next level.
                root.left.next = root.right
                if root.right:
                    if root.next:
                        if root.next.left:
                            root.right.next = root.next.left
                        else:
                            root.right.next = root.next.right
                else:
                    if root.next:
                        if root.next.left:
                            root.left.next = root.next.left
                        else:
                            root.left.next = root.next.right

            if root.right:
                if head == None: head = root.right
                if root.next:   # same as above if case inside right exists
                    if root.next.left:
                        root.right.next = root.next.left
                    else:
                        root.right.next = root.next.right
            root = root.next

        root = head

def connect_tree(root): # recursive
    # this is slight modification of postorder with updation of root.next.*, left.next and right.next
    if root:
        if root.left:
            if root.right:
                root.left.next = root.right
                if root.next:
                    # this loop is for the case where there are internal nodes with no childs
                    temp = root.next
                    while temp and temp.left == None and temp.right == None:
                        temp = temp.next

                    if temp and temp.left:
                        root.right.next = temp.left
                    elif temp and temp.right:
                        root.right.next = temp.right
            else:
                if root.next:
                    temp = root.next
                    while temp and temp.left == None and temp.right == None:
                        temp = temp.next

                    if temp and temp.left:
                        root.left.next = temp.left
                    elif temp and temp.right:
                        root.left.next = temp.right
        if root.right:
                if root.next:   # same as above if case inside right exists
                    if root.next.left:
                        root.right.next = root.next.left
                    else:
                        root.right.next = root.next.right

        connect_tree(root.right) # note, right child first to visit
        connect_tree(root.left)


def get_depth(root, data, level): # or get_level
    if root == None:
        return 0
    if root.data == data:
        return level
    l = get_depth(root.left, data, level+1)
    if l!=0: return l
    return get_depth(root.right, data, level+1)

def are_siblings(root, a, b):
    if root and root.left and root.right:
        if (root.left.data == a and root.right.data == b) or \
           (root.left.data == b and root.right.data == a):
            return True
        l = are_siblings(root.left, a, b)
        if l: return l
        return are_siblings(root.right, a, b)
    return False

def check_cousins(root, a, b):
    """
        find height of a
        find height of b
        if their heights equal, check their parent
        two nodes are said to be cousins if they are at the same level and both have
        different parents
    """
    level_of_a = get_depth(root, a, 0)
    level_of_b = get_depth(root, b, 0)
    return (
        (level_of_a == level_of_b and are_siblings(root, a, b)==False)
    )

def check_cousins_using_bfs(root, a, b):
    q = []
    bp = []
    q.append(root)

    while len(q) > 0:
        c = q.pop(0)
        if c.left and c.right:
            bp.append(c.left)
            bp.append(c.right)
            if (c.left.data == a and c.right.data == b) or \
                (c.left.data == b and c.right.data == a):
                return False # they have same parent, can't be cousins
        elif c.left:
            bp.append(c.left)
        elif c.left:
            bp.append(c.right)

        if len(q) == 0: # one level finished
            flag_a_found = False
            flag_b_found = False
            for v in bp:
                if v.data == a: flag_a_found = True
                if v.data == b: flag_b_found = True

            if flag_a_found and flag_b_found:
                return True
            q = bp[:]
            bp = []

    return False

def delete_leaves(root):
    if root:
        if root.left == None and root.right == None:
            return None
        root.left = delete_leaves(root.left)
        root.right = delete_leaves(root.right)

        return root

def is_same_tree(root_one, root_two):
    if root_one == None and root_two == None:
        return True
    elif root_one == None or root_two == None:
        return False
    else:
        return  root_one.data == root_two.data and \
                is_same_tree(root_one.left, root_two.left) and \
                is_same_tree(root_one.right, root_two.right)

def convert_sorted_llist_to_bt_O_NlogN(llist):

    def create_O_NlogN(head, start, end):
        if start >= end:
            return None
        mid = (start + end)//2
        print(start, mid, end)
        i=start
        t = head
        while i < mid and t.next != None:
            t = t.next
            i += 1

        root = Node(t.data)
        root.left = create_O_NlogN(head, start, mid)
        root.right = create_O_NlogN(t.next, mid+1, end) # key is .next and mid+1
        return root

    count = 0
    t = llist
    while t:
        count += 1
        t = t.next

    root = create_O_NlogN(llist, 0, count)
    return root

def convert_sorted_llist_to_bt_O_N(llist):

    def create_O_N(d, n):  # beauty !
        if n <= 0: return None
        left = create_O_N(d, n//2)

        root = Node(d['head'].data)
        root.left = left
        d['head'] = d['head'].next

        root.right = create_O_N(d, (n-(n//2)-1))
        return root

    count = 0
    t = llist
    while t:
        count += 1
        t = t.next

    d = {'head': llist}
    root = create_O_N(d, count)
    return root


def is_avl_tree(root):
    # avl tree is a binary tree with below condition
    # for every node, abs(height (left) - height(right)) <= 1
    if root:
        return \
            is_avl_tree(root.left) and is_avl_tree(root.right) and \
            abs(height(root.left)-height(root.right)) <= 1
    return True


def root_to_leaf_path_sum(root, sum):
    if sum == 0:
        return True
    if root:
        l = root_to_leaf_path_sum(root.left, sum-root.data)
        if l: return True

        r = root_to_leaf_path_sum(root.right, sum-root.data)
        if r: return True

        return False
    return False

def mirror_image(root):
    if root:
        mirror_image(root.left)
        mirror_image(root.right)

        temp = root.left
        root.left = root.right
        root.right = temp

def is_sub_tree(t1, t2):  # checks T2 is sub tree of T1
    if t2 == None:
        return True
    if t1 == None:
        return False
    if is_same_tree(t1, t2):
        return True

    return is_sub_tree(t1.left, t1) or is_sub_tree(t1.right, t2)

def get_difference_sumof_all_odd_and_even_levels(root):
    if root:
        return \
            root.data - \
            get_difference_sumof_all_odd_and_even_levels(root.left) - \
            get_difference_sumof_all_odd_and_even_levels(root.right)
    return 0


def print_all_paths(root):

    def paths(root, path):
        if root:
            p = path + [root.data]
            if root.left == None and root.right == None:
                print(p)
                return
            paths(root.left, p)
            paths(root.right, p)

    path = []
    paths(root, path)


def diameter_O_N_2(root):
    if root:
        lh = height(root.left)
        rh = height(root.right)

        cd = lh + rh + 1
        ld = diameter_O_N_2(root.left)
        rd = diameter_O_N_2(root.right)

        return max(cd, ld, rd)
    return 0

def diameter_O_N(root): # finds the height at the same time
    # O(N) but O(N) space as it keeps 4 varaibles on stack
    # for every recursive call.
    def diameter(root, height):
        #http://www.crazyforcode.com/diameter-tree/
        lh = {'v': 0}
        rh = {'v': 0}
        ld = {'v': 0}
        rd = {'v': 0}

        if root == None:
            height['v'] = 0
            return 0

        ld['v'] = diameter(root.left, lh)
        rd['v'] = diameter(root.right, rh)

        height['v'] = max(lh['v'], rh['v']) + 1

        return max(lh['v']+rh['v']+1, ld['v'], rd['v'])

    height = {'v': 0}
    return diameter(root, height)

def diameter_with_bfs(root):
    # idea comes from Do exercise 22.2-7 on page 539 of CLRS
    """
        Run BFS on any node S in the graph, remembering the node U discovered last.
        Run BFS from U remembering the node V discovered last.
        D(U, V) is the diameter of the Graph
        links:
        http://techieme.in/tree-diameter/
        # traverse post order and update the node heights and their max
        # distance betweeen leaf nodes.
        Steps to solve
        1) Initialize all the leaves with leftHeight and rightHeight as 1.
        2) Initialize all the leaves with maxDistance as 0, we make it a point that if either of the leftHeight or rightHeight is 1 we make the maxDistance = 0
        3) Move upward one at a time and calculate the values for the immediate parent. It would be easy because now we know these values for the children.
        4) At a given node,
        a) assign leftHeight as maximum of (leftHeight or rightHeight of its left child).
        b) assign the rightHeight as maximum of (leftHeight or rightHeight of its right child).
        c) if any of these values (leftHeight or rightHeight) is 1 make the maxDistance as zero.
        d) if both the values are greater than zero make the maxDistance as leftHeight + rightHeight – 1
        5) Maintain the maxDistance in a temp variable and if in step 4 the maxDistance is more than the current value of the variable, replace it with the new maxDistance value.
        6) At the end of the algorithm the value in maxDistance is the diameter.
    """
    s = []
    o = []
    dist = 0

    # insert nodes in dfs order so that it ends up having childs to pop
    # first than internal nodes.
    s.append(root)
    while len(s) > 0:
        c = s.pop()
        o.append(c)

        if c.left:
            s.append(c.left)
        if c.right:
            s.append(c.right)

    print([x.data for x in o])
    while len(o) > 0:
        c = o.pop()
        #print(c.data)
        one = False
        if c.left == None:
            c.left_height = 1
            one = True
        else:
            c.left_height = max(c.left.left_height, c.left.right_height) + 1

        if c.right == None:
            c.right_height = 1
            one = True
        else:
            c.right_height = max(c.right.right_height, c.right.left_height) + 1

        if one:
            # we can set max distance possible from c to 0
            pass
        else:
            temp = c.left_height + c.right_height - 1
            if dist < temp:
                dist = temp
    return dist


def sum_left_and_right_subtrees(root):
    """
    Replace each node with sum of values in left and right subtree.
    leaf nodes value will be changed to 0
    """
    if root:
        old_value = root.data
        new_value = sum_left_and_right_subtrees(root.left) + \
                    sum_left_and_right_subtrees(root.right)
        root.data = new_value
        return old_value + new_value

    return 0

def check_children_sum_property(root):
    """each node sum of its left and right children should be equal to node value"""
    if root:
        if root.left == None and root.right == None:
            return True

        left_sum = 0
        right_sum = 0

        if root.left:
            left_sum = root.left.data

        if root.right:
            right_sum = root.right.data

        if root.data != (left_sum + right_sum):
            return False

        if not check_children_sum_property(root.left) or \
            not check_children_sum_property(root.right):
            return False
        return True


    return True







# Test(s)
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

    data = [5, 3, 7, 1, 4, 6, 9]
    root = None
    for d in data:
        root = insert(root, d)

    print("\n")
    inorder(root)
    print("\n")
    ll = to_doubly_linked_list_sol2(root)
    print_dll(ll)



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

def test_13():
    data = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49, 65, 39]
    root = None
    for d in data:
        root = insert(root, d)

    get_range(root, 10, 18)
    print("\n")
    get_range(root, 10, 43)

    print("\n")
    print_nodes_at_level(root, 1)
    print("\n")
    print_nodes_at_level(root, 2)
    print("\n")
    print_nodes_at_level(root, 3)
    print("\n")
    print_nodes_at_level(root, 4)
    print("\n")
    print_nodes_at_level(root, 5)

def test_14():
    data = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49]
    root = None
    for d in data:
        root = insert(root, d)
    d = get_parenthesis_representation(root)
    print(d)

    rt = create_from_parenthesis(d)
    print("\ninorder:", end='')
    inorder(rt)
    connect_tree(rt)
    print("\nLevel order using queue:        ", end='')
    bfs(rt)
    print("\nLevel order using next pointers:", end='')
    print_level_order_using_pointers(rt)

    print("\nusing non recursive version")
    rt = create_from_parenthesis(d)
    connect_tree_non_recursive(rt)
    print("Level order using queue:        ", end='')
    bfs(rt)
    print("\nLevel order using next pointers:", end='')
    print_level_order_using_pointers(rt)
    print("\n")


    d = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    root = None
    for v in d:
        root = insert(root, v)
    d = get_parenthesis_representation(root)
    rt = create_from_parenthesis(d)
    bfs(rt)
    connect_tree_non_recursive(rt)
    print("\n")
    print_level_order_using_pointers(rt)

    rt = create_from_parenthesis(d)
    connect_tree(rt)
    print("\n")
    print_level_order_using_pointers(rt)

def test_15():
    d = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    root = None
    for v in d:
        root = insert(root, v)

    """
                        10        -----------------level 0
                      9   11                       level 1
                    8       12                     level 2
                   7          13                   level 3
                 6              14                 level 4
               5                  15               level 5
             4                      16             level 6
           3                          17           level 7
          2                             18         level 8
        1                                  19      level 9

    """
    print(get_depth(root, 18, 0))
    print(get_depth(root, 1, 0))
    print(get_depth(root, 6, 0))
    print(get_depth(root, 10, 0))


def test_16():
    data = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49]
    root = None
    for d in data:
        root = insert(root, d)

    print(are_siblings(root, 16, 18))
    print(are_siblings(root, 16, 31))
    print(are_siblings(root, 17, 49))
    print(are_siblings(root, 43, 19))
    print(are_siblings(root, 8, 17))
    print(are_siblings(root, 3, 5))
    print(are_siblings(root, 4, 8))
    print(are_siblings(root, 6, 19))
    print(are_siblings(root, 17, 43))
    print(are_siblings(root, 31, 49))

def test_17():
    data = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49]
    root = None
    for d in data:
        root = insert(root, d)

    print(check_cousins(root, 4, 8))
    print(check_cousins(root, 8, 43))
    print(check_cousins(root, 8, 17))
    print(check_cousins(root, 16, 18))
    print(check_cousins(root, 5, 49))

    print("\n")
    print(check_cousins_using_bfs(root, 4, 8))
    print(check_cousins_using_bfs(root, 8, 43))
    print(check_cousins_using_bfs(root, 8, 17))
    print(check_cousins_using_bfs(root, 16, 18))
    print(check_cousins_using_bfs(root, 5, 49))

def test_18():
    data = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49]
    root = None
    for d in data:
        root = insert(root, d)

    bfs_spiral_order_using_queues(root)
    print("\n")
    print_spiral_order_using_stacks(root)
    print("\n")
    print_spiral_order_using_recursion(root)

def test_19():
    data = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49]
    root = None
    for d in data:
        root = insert(root, d)

    bfs_recursion(root)

def test_20():
    data = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49]
    root = None
    for d in data:
        root = insert(root, d)

    delete_leaves(root)
    inorder(root)

def test_21():
    data = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49]
    root = None
    for d in data:
        root = insert(root, d)

    data = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18]
    another = None
    for d in data:
        another = insert(another, d)

    print(is_same_tree(root, another))


def test_22():
    class LNode:
        def __init__(self, data):
            self.data = data
            self.next = None

    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    l1 = [1, 2, 3, 4, 5]

    head = None
    for i in l[::-1]:
        t = LNode(i)
        t.next = head
        head = t

    root = convert_sorted_llist_to_bt_O_NlogN(head)
    inorder(root)
    print("\n")
    print(height(root))
    bfs_spiral_order_using_queues(root)


    r = convert_sorted_llist_to_bt_O_N(head)
    inorder(r)
    print("\nHeight:", height(r))

    bfs_spiral_order_using_queues(r)

def test_23():
    l = [5, 3, 7, 1, 4, 6, 9]
    root = None
    for d in l:
        root = insert(root, d)
    print(is_avl_tree(root))

    delete(root, 6)
    print(is_avl_tree(root))

    delete(root, 9)
    print(is_avl_tree(root))

    delete(root, 7)
    print(is_avl_tree(root))

def test_24():
    l = [5, 3, 7, 1, 4, 6, 9]
    root = None
    for d in l:
        root = insert(root, d)

    print(root_to_leaf_path_sum(root, 21))
    print(root_to_leaf_path_sum(root, 18))
    print(root_to_leaf_path_sum(root, 12))
    print(root_to_leaf_path_sum(root, 8))
    print(root_to_leaf_path_sum(root, 38))
    print(root_to_leaf_path_sum(root, 3))

def test_25():
    l = [5, 3, 7, 1, 4, 6, 9]
    root = None
    for d in l:
        root = insert(root, d)

    inorder(root)
    mirror_image(root)
    print("\n")
    inorder(root)

def test_26():
    l = [5, 3, 7, 1, 4, 6, 9]
    t1 = None
    for d in l:
        t1 = insert(t1, d)
    inorder(t1)

    l = [7, 6, 9]
    t2 = None
    for d in l:
        t2 = insert(t2, d)
    inorder(t2)
    print("\n")
    print(is_sub_tree(t1, t2))


def test_27():
    l = [5, 3, 7, 1, 4, 6, 9]
    root = None
    for d in l:
        root = insert(root, d)

    print(get_difference_sumof_all_odd_and_even_levels(root))

    l = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49]
    root = None
    for d in l:
        root = insert(root, d)
    bfs_spiral_order_using_queues(root)
    print(get_difference_sumof_all_odd_and_even_levels(root))


def test_28():
    l = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49]
    root = None
    for d in l:
        root = insert(root, d)

    print_all_paths(root)

def test_29():
    l = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49]
    root = None
    for d in l:
        root = insert(root, d)

    print(diameter_O_N_2(root)) # 7

    l = [8, 3, 9, 2, 5, 10, 4, 6, 24, 16, 50, 12, 18]
    root = None
    for d in l:
        root = insert(root, d)

    print(diameter_O_N_2(root))  # 9

    l = [16, 8, 20, 3, 9, 46, 2, 7, 12, 5, 10, 14, 4, 6, 10, 15]
    root = None
    for d in l:
        root = insert(root, d)
    print(diameter_O_N_2(root))  # 9

    print('Diameter: ')
    print(diameter_O_N(root))  # 9

    l = [16, 8, 20, 3, 9, 46, 2, 7, 12, 5, 10, 14, 4, 6, 10, 15]
    class ExtenedNode:
        def __init__(self, data):
            self.data = data
            self.left = self.right = None
            self.left_height = None
            self.right_height = None

    def cinsert(root, data):
        if root == None:
            return ExtenedNode(data)
        if data < root.data:
            root.left = cinsert(root.left, data)
        elif data > root.data:
            root.right = cinsert(root.right, data)
        # we dont insert duplicates
        return root

    root = None
    for d in l:
        root = cinsert(root, d)
    print(diameter_with_bfs(root))

def test_30():
    l = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49]
    root = None
    for d in l:
        root = insert(root, d)

    inorder(root)
    print("\n")
    print(sum_left_and_right_subtrees(root))
    print("\n")
    inorder(root)

def test_31():
    l = [37]
    root = None
    for d in l:
        root = insert(root, d)

    inorder(root)
    print("\n")
    print(check_children_sum_property(root))

def test_32():
    d = [5, 3, 8, 2, 4, 7]
    root = None
    for v in d:
        root = insert(root, v)

    #print(inorder_predecessor(root, 2).data)  # None
    print(inorder_predecessor(root, 4).data)  # 3
    print(inorder_predecessor(root, 3).data)  # 2
    print(inorder_predecessor(root, 7).data)  # 5
    print(inorder_predecessor(root, 8).data)  # 7

    #print(inorder_predecessor_bt(root, 2).data)  # None
    print(inorder_predecessor_bt(root, 4).data)  # 3
    print(inorder_predecessor_bt(root, 3).data)  # 2
    print(inorder_predecessor_bt(root, 7).data)  # 5
    print(inorder_predecessor_bt(root, 8).data)  # 7

    d = [5, 3, 8, 2, 4, 9, 10, 12, 11]
    root = None
    for v in d:
        root = insert(root, v)
    print(inorder_predecessor(root, 11).data)  # 10
    print(inorder_predecessor_bt(root, 11).data)  # 10

def test_33():
    d = [5, 3, 8, 2, 4, 7]
    root = None
    for v in d:
        root = insert(root, v)

    print(inorder_successor(root, 4).data)  # 5
    print(inorder_successor(root, 3).data)  # 5
    print(inorder_successor(root, 2).data)  # 3
    print(inorder_successor(root, 5).data)  # 7
    #print(inorder_successor(root, 8).data)  # None

    print(inorder_successor_bt(root, 4).data)  # 5
    print(inorder_successor_bt(root, 3).data)  # 5
    print(inorder_successor_bt(root, 2).data)  # 3
    print(inorder_successor_bt(root, 5).data)  # 7
    #print(inorder_successor_bt(root, 8).data)  # None

    d = [6, 1, 8, 3, 2, 4]
    root = None
    for v in d:
        root = insert(root, v)

    print(inorder_successor(root, 4).data)  # 6
    print(inorder_successor_bt(root, 4).data)  # 6

test_33()