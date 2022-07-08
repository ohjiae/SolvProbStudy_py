from collections import deque
N, M = map(int, input().split())
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    indegree[e] += 1
    graph[s].append(e)
def topology_sort():
    q = deque([])
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        cur = q.popleft()
        print(cur, end=' ')
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
topology_sort()