from lib.util import swap

def qsort(a):

    def _qsort(a, left, right):
        if left >= right:
            return

        mid = (left + right)//2
        swap(a, left, mid)

        # Partition
        last = left
        i = left + 1
        while i <= right:
            if a[i] < a[left]:
                last += 1
                swap(a, i, last)
            i += 1
        swap(a, left, last)

        # recurse
        _qsort(a, left, last-1)
        _qsort(a, last+1, right)


    _qsort(a, 0, len(a)-1)

a = [4, 5, 2, 6, 9, 10, 1, 3, 8, 7]
print(a)
qsort(a)
print(a)