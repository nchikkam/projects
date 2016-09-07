from lib.util import swap

def merge_sort(a):

    def combine(a, b):
        c = []
        while len(a) != 0 and len(b) != 0:
            if a[0] < b[0]:
                c.append(a.pop(0))
            else:
                c.append(b.pop(0))
        if len(a) == 0:
            c += b
        else:
            c += a
        return c

    def merge(a):
        if len(a) == 0 or len(a) == 1:
            return a
        else:
            mid = len(a) // 2
            c = merge(a[:mid])
            d = merge(a[mid:])
            return combine(c, d)

    _sorted = merge(a)
    for i, v in enumerate(_sorted):
        a[i] = v

a = [4, 5, 2, 6, 9, 10, 1, 3, 8, 7]
print(a)
merge_sort(a)
print(a)