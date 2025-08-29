import sys
import heapq

def constructAdj(edges, V):
    adj = [[] for _ in range(V)]
    for u, v, w in edges: #u = start, v = end, w = weight.
        adj[u].append((v, w))
    return adj

def dijkstra(V, edges, src):
    adj = constructAdj(edges, V)
    pq = []
    dist = [sys.maxsize] * V
    dist[src] = 0
    heapq.heappush(pq, (0, src)) #distance, node

    while pq:
        d, u = heapq.heappop(pq)
        if d>dist[u]:
            continue
        for v, weight in adj[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    return dist

if __name__ == "__main__":
    V, E = map(int, input("Enter number of vertices and edges: ").split())
    edges = []
    print("Enter edges in format: u v w")
    for _ in range(E):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    src = int(input("Enter source vertex: "))

    distances = dijkstra(V, edges, src)
    print("\nShortest distances from source", src, ":")
    for i, d in enumerate(distances):
        print(f"{src} → {i} = {d if d != sys.maxsize else 'INF'}")