def susets(str, size):

    def get_binary_slow(n, ret):
        while n > 0:
            rem = n % 2
            n = n//2
            ret.append(rem)
        return list(reversed(ret))

    def get_binary(n, p):
        ret = [0] * p
        for i in range(p):
            m = 1 << i
            if n&m!=0:
                ret[i] =1
            else:
                ret[i] = 0
        return list(reversed(ret))

    def print_subset(l, elements):
        for i, v in enumerate(elements):
            if v == 1:
                print(l[i], end='')
        print("\n")

    def _subsets(l, size):
        p = 2**len(l)
        for x in range(p):
            elements = get_binary(x, len(l))

            if elements.count(1) == size:
                print_subset(l, elements)

    l = list(str)
    _subsets(l, size)

susets("abcde", 3)