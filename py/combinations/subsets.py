def subsets(str, size):

    def _subsets(l, start, end, size, sset):
        if size == 0:
            print(sset)
        else:
            for pos in range(start, end):
                sset.append(l[pos])
                _subsets(l, pos+1, end, size-1, sset)
                sset.pop()

    l = list(str)
    _subsets(l, 0, len(l), size, [])

subsets("abcde", 5)