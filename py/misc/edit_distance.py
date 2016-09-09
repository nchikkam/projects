def insertCost(x):
    return 1

def deleteCost(x):
    return 1

def substCost(x, y):
    if x==y: return 0
    return 1

def minEditDist(target, source):
    ''' Computes the min edit distance from target to source. Figure 3.25 '''

    n = len(target)
    m = len(source)

    distance = [[0 for i in range(m + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        distance[i][0] = distance[i - 1][0] + insertCost(target[i - 1])

    for j in range(1, m + 1):
        distance[0][j] = distance[0][j - 1] + deleteCost(source[j - 1])

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            distance[i][j] = min(distance[i - 1][j] + 1,
                                 distance[i][j - 1] + 1,
                                 distance[i - 1][j - 1] + substCost(source[j - 1], target[i - 1]))
    return distance[n][m]

print(minEditDist("trails", "Zeil"))