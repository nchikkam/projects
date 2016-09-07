from lib.util import swap

"""
        a
      /   \
     b     c
     at any time we have 3 nodes to compare,
     root, its left and right. min heap preserves
     the constraint that root is min than its child
     where as max heap preserves that root is max
     than its childs.

     For simplicity we assume array starts at index: 1
"""
def heapify(a, root, l):
    left    = 2*root
    right   = (2*root)+1
    max_index = root

    # make root's value max(root, left, right)
    if left < l and a[root] < a[left]:
        max_index = left
    if right < l and a[max_index] < a[right]:
        max_index = right

    if max_index != root:
        swap(a, root, max_index)
        heapify(a, max_index, l)

def heap_sort(a):
    l = len(a)-1
    mid = l//2
    for i in list(range(mid, 0, -1)):   # O(nlogn)
        heapify(a, i, l)  # log n

    print(a)
    for i in list(range(l, 0, -1)):
        swap(a, 1, i)
        heapify(a, 1, i)
        print(a)

# 0th element is dummy
a = [None, 4, 5, 2, 6, 9, 10, 1, 3, 8, 7]
print(a)
heap_sort(a)
print(a)