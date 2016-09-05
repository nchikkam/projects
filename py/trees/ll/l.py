class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_llist(current, basket):
    if current:
        if current.next == None:
            basket['start'] = current
        else:

            next_node = reverse_llist(current.next, basket)
            next_node.next = current

            current.next = None # tricky one
            # doing above sets the initial head's next to None

        return current

def print_llist(head):
    while head:
        print("{} ".format(head.data), end='')
        head = head.next
    print("\n")

def swap_every_two_nodes(head):
    """
        http://www.programcreek.com/2014/04/leetcode-swap-nodes-in-pairs-java/
        idea: think outside the box.
        Add an extra node at the begining
    """
    if head == None or head.next == None:
        return head

    h = Node(None)   # dummy node
    h.next = head
    p = h

    while p.next and p.next.next:
        t1 = p
        p = p.next
        t1.next = p.next

        t2 = p.next.next
        p.next.next = p
        p.next = t2

    return h.next

def swap_every_two_nodes_recursive(head): # stack goes high
    if head == None or head.next == None:
        return head
    h = head.next
    head.next = swap_every_two_nodes_recursive(head.next.next)
    h.next = head
    return h

def swap_every_two_nodes_using_stack(head):

    if head == None or head.next == None:
        return head

    stack = []
    ret = head.next
    prev = None
    while head.next:
        if len(stack) == 2:
            a = stack.pop()
            b = stack.pop()

            a.next = b
            b.next = head

            if prev:
                prev.next = a
            prev = b
        stack.append(head)
        head = head.next

    return ret


def test():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    basket = {}
    ll = Node(l[0])
    head = ll
    for i in range(1, len(l)):
        ll.next = Node(l[i])
        ll = ll.next
    ll.next = None
    print_llist(head)

    reverse_llist(head, basket)
    rev_head = basket['start']

    print_llist(rev_head)

def test_one():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ll = Node(l[0])
    head = ll
    for i in range(1, len(l)):
        ll.next = Node(l[i])
        ll = ll.next
    ll.next = None
    print("actual:")
    print_llist(head)

    r = swap_every_two_nodes(head)
    print("non-recursive:")
    print_llist(r)

    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ll = Node(l[0])
    head = ll
    for i in range(1, len(l)):
        ll.next = Node(l[i])
        ll = ll.next
    ll.next = None
    r = swap_every_two_nodes_recursive(head)
    print("recursive:")
    print_llist(r)

    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ll = Node(l[0])
    head = ll
    for i in range(1, len(l)):
        ll.next = Node(l[i])
        ll = ll.next
    ll.next = None
    r = swap_every_two_nodes_using_stack(head)
    print("stack:")
    print_llist(r)

test_one()