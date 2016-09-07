g = {
    'a': ['b', 'c'],
    'b': ['e', 'g'],
    'c': ['f'],
    'd': ['a', 'b', 'c', 'f', 'g'],
    'e': [],
    'f': [],
    'g': ['e']
}

h = {
    "a": ["b", "c", "d"],
    "b": [],
    "c": ["d"],
    "d": [],
    "e": ["g", "f", "q"],
    "g": [],
    "f": [],
    "q": []
}

cycle_graph = {
    'a': ['b', 'c'],
    'b': ['e', 'g'],
    'c': ['f'],
    'd': ['a', 'b', 'c', 'f', 'g'],
    'e': [],
    'f': [],
    'g': ['e', 'a']

}

def topological(graph):

    visited = {}
    res = {'order':[]}
    def dfs(graph, u): # dfs with starting node 'u'
        visited[u] = True

        for v in graph[u]: # for all neighbor's of 'u'
            if v not in visited:
                dfs(graph, v)

        res['order'].append(u)

    def traverse(graph):
        visited.clear()

        for u in graph.keys():
            if not u in visited:
                dfs(graph, u)

    traverse(graph)
    res['order'].reverse()
    return res['order']

print(topological(g))
print(topological(h))
#print(topological(cycle_graph))