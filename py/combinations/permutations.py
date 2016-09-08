def permutations(str):
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def _perm(l, start, end):
        if start == end:
            print(l)
        else:
            for i in range(start, end):
                swap(l, start, i)
                _perm(l, start+1, end)
                swap(l, start, i)

    l = list(str)
    _perm(l, 0, len(l))

permutations("abc")