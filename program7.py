class ShortestPath:
    def __init__(self, V, edges):
        self.V = V
        self.edges = edges

    # Dijkstra's Algorithm
    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        visited = [False] * self.V

        for _ in range(self.V):
            u = -1

            for i in range(self.V):
                if not visited[i] and (u == -1 or dist[i] < dist[u]):
                    u = i

            if u == -1 or dist[u] == float('inf'):
                break

            visited[u] = True

            for v, w in self.edges[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        return dist

    # Bellman-Ford Algorithm
    def bellman_ford(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for u in range(self.V):
                for v, w in self.edges[u]:
                    if dist[u] != float('inf') and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w

        for u in range(self.V):
            for v, w in self.edges[u]:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    return "Negative cycle detected"

        return dist


# Main Program

edges = [
    [(1, 4), (2, 1)],
    [(3, 1)],
    [(1, 2), (3, 5)],
    []
]

g = ShortestPath(4, edges)

print("Dijkstra:", g.dijkstra(0))
print("Bellman-Ford:", g.bellman_ford(0))
