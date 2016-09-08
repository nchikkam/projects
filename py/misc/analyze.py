inf = 2**32
def analyze(g):
    l = len(g)
    src = None
    for i in range(l):
        for j in range(l):
            if g[i][j] != 0 and g[i][j] != inf:
                src = i
    d = {}
    s = {}
    p = {}
    t = []

    for i in range(l):
        d[i] = g[src][i]
        s[i] = 0
        p[i] = src

    s[src] = 1
    _sum = 0
    k = 0
    for i in range(1, l):
        u = -1
        m = inf
        for j in range(l):
            if s[j] == 0:
                if d[j] <= m:
                    m = d[j]
                    u = j

        t.append((u, p[u]))
        k += 1
        _sum += g[u][p[u]]

        s[u] = 1
        for v in range(l):
            if s[v]==0 and g[u][v] < d[v]:
                d[v] = g[u][v]
                p[v] = u

    if _sum > inf:
        print("Can't Analyze, Check the Connections")
    else:
        for conn in t:
            print(conn)
        print(_sum)


# class 2
data = [
    (0, 1, 60),
    (0, 2, 10),
    (1, 3, 20),
    (1, 4, 40),
    (1, 5, 70),
    (2, 5, 50),
    (3, 5, 80),
    (4, 5, 30)
]
g = [[inf] * 6 for x in range(6)]
for s, d, c in data:
    if s == d:
        g[s][d] = 0
    else:
        g[s][d] = c
        g[d][s] = c

analyze(g)


# class 3
data = [
    (0, 1, 10),
    (0, 2, 20)
]
g = [[inf] * 4 for x in range(4)]
for s, d, c in data:
    if s == d:
        g[s][d] = 0
    else:
        g[s][d] = c
        g[d][s] = c

analyze(g)