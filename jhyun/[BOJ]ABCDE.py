N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
def dfs(visit: list, cur, depth):
    if depth == 4:
        print(1)
        exit(0)
    for nxt in graph[cur]:
        if not visit[nxt]:
            visit[cur] = True
            dfs(visit, nxt, depth + 1)
            visit[cur] = False
for i in range(N):
    visit = [False] * N
    dfs(visit, i, 0)
print(0)