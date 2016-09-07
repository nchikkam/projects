from lib.util import swap

def selection_sort(a):
    # swaps once with min_index
    l = len(a)
    for i in range(l):
        min_index = i
        for j in range(i+1, l):
            if a[min_index] > a[j]:
                min_index = j
        swap(a, i, min_index)

a = [4, 5, 2, 6, 9, 10, 1, 3, 8, 7]
print(a)
selection_sort(a)
print(a)