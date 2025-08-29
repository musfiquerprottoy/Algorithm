def dijkstra(V, edges, src):
    adj = constructAdj(edges, V)
    pq = []
    dist = [sys.maxsize] * V
    heapq.heappush(pq, [0, src])
    dist[src] = 0

    while pq:
        u = heapq.heappop(pq)[1]
        for x in adj[u]:
            v, weight = x[0], x[1]

            if dist[V] > dist[u]:
                dist[V] = dist[u] + weight
                heapq.heappush(pq, [dist[v], V])
                return dist