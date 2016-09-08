def print_booleans(l):
    for v in l:
        if v == True:
            print(1, end='')
        else:
            print(0, end='')
    print()

def binary(width):
    r = 2**width

    flags = [False] * width
    base  = [2**x for x in range(width-1, -1, -1)]
    counts= [2**x for x in range(width-1, -1, -1)]

    for i in range(r):
        print_booleans(flags)

        for j in range(width):
            counts[j] -= 1
            if counts[j] == 0:
                flags[j] = not flags[j] # reset
                counts[j] = base[j]     # restore counts value from base backup

binary(4)