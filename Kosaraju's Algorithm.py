from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

# DFS and push to stack by finishing time
    def _dfs_fill(self, v, visited, stack):
        visited[v] = True
        for nei in self.graph[v]:
            if not visited[nei]:
                self._dfs_fill(nei, visited, stack)
        stack.append(v)

    # Step 2: Transpose the graph (reverse all edges)
    def transpose(self):
        g_t = Graph(self.V)
        for u in self.graph:
            for v in self.graph[u]:
                g_t.addEdge(v, u)
        return g_t

    # Step 3: DFS for collecting SCC
    def _dfs_collect(self, v, visited, component):
        visited[v] = True
        component.append(v)
        for nei in self.graph[v]:
            if not visited[nei]:
                self._dfs_collect(nei, visited, component)

    def kosaraju(self):
        stack = []
        visited = [False] * self.V

    #Fill stack by finishing times
        for i in range(self.V):
            if not visited[i]:
                self._dfs_fill(i, visited, stack)
        gr = self.transpose()
        visited = [False] * self.V
        sccs = []

        while stack:
            v = stack.pop()
            if not visited[v]:
                component = []
                gr._dfs_collect(v, visited, component)
                sccs.append(component)

        return sccs


if __name__ == "__main__":
    V, E = map(int, input("Enter number of vertices and edges: ").split())
    g = Graph(V)
    print("Enter edges (u v):")
    for _ in range(E):
        u, v = map(int, input().split())
        g.addEdge(u, v)

    sccs = g.kosaraju()
    print("\nStrongly Connected Components:")
    for comp in sccs:
        print(comp)
'''
Test case:
Enter number of vertices and edges: 5 5
Enter edges (u v):
1 0
0 2
2 1
0 3
3 4
'''