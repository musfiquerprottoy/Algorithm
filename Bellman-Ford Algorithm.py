import sys

def bellmanFord(V, edges, src):
    dist = [sys.maxsize] * V
    dist[src] = 0

    for _ in range(V - 1):
        for u, v, w in edges:
            if dist[u] != sys.maxsize and dist[u] + w < dest[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] != sys.maxsize and dist[u] + w <dist[v]
            print("Graph contains a negative weight cycle.")
            return None
    return dist

if __name__== "__main__":
    v, e = map(int, input("Enter number of vertices and edges:").split())
    edges = []
    print("Enter edges in format: u, v, w")
    for _ in range(e):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    src = int(input("Enter source vertex:"))
    distances = (bellmanFord, edges, src)
    if distances:
        print("\nShortest distances from source:", src, ":")
        for i, d in enumerate(distances):
            print(f"{src} --> {i} = {d if d!=sys.maxsize else 'INF'}")
