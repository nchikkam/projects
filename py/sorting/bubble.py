from lib.util import swap

def bubble_sort(a):
    # swaps each time
    l = len(a)
    for i in range(l):
        for j in range(i+1, l):
            if a[i] > a[j]:
                swap(a, i, j)

a = [4, 5, 2, 6, 9, 10, 1, 3, 8, 7]
print(a)
bubble_sort(a)
print(a)