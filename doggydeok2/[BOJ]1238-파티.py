import heapq


def dijkstra(_adl):
    dij = [float('inf')] * (N + 1)
    prq = [(0, X)]
    dij[X] = 0
    while prq:
        t, e = heapq.heappop(prq)
        if dij[e] < t:
            continue
        for nxt in _adl[e]:
            nt, ne = nxt
            if t + nt < dij[ne]:
                dij[ne] = t + nt
                heapq.heappush(prq, (t + nt, ne))
    return dij


N, M, X = map(int, input().split())
go_adl = [[] for _ in range(N + 1)]
from_adl = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    go_adl[s].append((t, e))
    from_adl[e].append((t, s))

gotoX = dijkstra(go_adl)
fromtoX = dijkstra(from_adl)
print(max([gotoX[i] + fromtoX[i] for i in range(1, N + 1)]))
