import heapq


def solution(N, road, K):
    dist = [int(1e9) for _ in range(N + 1)]
    dist[1] = 0
    adl = [[] for _ in range(N + 1)]
    for s, e, t in road: 
        adl[s].append((t, e))
        adl[e].append((t, s))
        
    prq = [(0, 1)]
    while prq:
        t, e = heapq.heappop(prq)
        if dist[e] < t:
            continue
        for nt, ne in adl[e]:
            print(ne, t + nt)
            if dist[ne] < t + nt:
                continue
            dist[ne] = t + nt
            heapq.heappush(prq, (t + nt, ne))
    return sum([dist[i] <= K for i in range(1, N + 1)])