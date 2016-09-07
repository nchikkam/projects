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
    min_index = root


    if left < l and a[root] < a[left]:
        min_index = left
    if right < l and a[min_index] < a[right]:
        min_index = right

    if min_index != root:
        swap(a, root, min_index)
        heapify(a, min_index, l)

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