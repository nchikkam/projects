from lib.util import swap

def insertion_sort(a):
    # insert j'th element to right spot on its left
    l = len(a)
    for i in range(1, l):
        j = i
        while j > 0 and a[j] < a[j-1]:
            swap(a, j, j-1)
            j -= 1

a = [4, 5, 2, 6, 9, 10, 1, 3, 8, 7]
print(a)
insertion_sort(a)
print(a)