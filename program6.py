class Graph:
    def __init__(self, V):
        self.V = V
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((w, u, v))

    def kruskal_mst(self):
        parent = list(range(self.V))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        result = []

        for w, u, v in sorted(self.edges):
            a, b = find(u), find(v)

            if a != b:
                result.append((u, v, w))
                parent[a] = b

        return result

    def prim_mst(self):
        visited = [False] * self.V
        visited[0] = True
        result = []

        while len(result) < self.V - 1:
            edge = None

            for w, u, v in self.edges:
                if visited[u] != visited[v]:
                    if edge is None or w < edge[0]:
                        edge = (w, u, v)

            if edge is None:
                break

            w, u, v = edge
            result.append((u, v, w))
            visited[u] = visited[v] = True

        return result


g = Graph(4)

g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

print("Kruskal:", g.kruskal_mst())
print("Prim:", g.prim_mst())

    print("Kruskal's MST:")
    print(g.kruskal_mst())
    
    print("\nPrim's MST:")
    print(g.prim_mst())
