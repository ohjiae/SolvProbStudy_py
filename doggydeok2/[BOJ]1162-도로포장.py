import heapq
import sys
rl = sys.stdin.readline


N, M, K = map(int, rl().split())
dist = [[float('inf')] * (K + 1) for _ in range(N + 1)]
dist[1][0] = 0

adl = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, t = map(int, rl().split())
    adl[s].append((t, e))
    adl[e].append((t, s))

q = [(0, 1, 0)]
while q:
    t, s, wrapped = heapq.heappop(q)
    if t > dist[s][wrapped]:
        continue
    for nxt in adl[s]:
        nt, ns = nxt
        if t + nt < dist[ns][wrapped]:
            dist[ns][wrapped] = t + nt
            heapq.heappush(q, (t + nt, ns, wrapped))
        if wrapped < K and t < dist[ns][wrapped + 1]:
            dist[ns][wrapped + 1] = t
            heapq.heappush(q, (t, ns, wrapped + 1))
print(min(dist[-1]))
