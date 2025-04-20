import heapq

n, m, K = map(int, input().split())
c = list(map(int, input().split()))
g = [[] for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    g[u - 1].append((v - 1, c[i]))
    g[v - 1].append((u - 1, c[i]))


def dijkstra(start):
    dist = [[float("inf")] * (K + 1) for _ in range(n)]
    dist[start][0] = 0
    hq = [(0, start, 0)]
    while hq:
        d, u, k = heapq.heappop(hq)
        if d > dist[u][k]:
            continue
        for v, w in g[u]:
            if k + 1 <= K and dist[v][k + 1] > d:
                dist[v][k + 1] = d
                heapq.heappush(hq, (d, v, k + 1))
            if dist[v][k] > d + w:
                dist[v][k] = d + w
                heapq.heappush(hq, (d + w, v, k))
    return dist


dist = dijkstra(0)
ans = min(dist[n - 1])
print(-1 if ans == float("inf") else ans)
