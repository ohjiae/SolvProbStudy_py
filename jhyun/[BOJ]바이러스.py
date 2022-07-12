from collections import deque
N = int(input())
edge = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(edge):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
def bfs(start: int):
    q = deque([start])
    visit = [False] * (N + 1)
    visit[start] = True
    result = 0
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visit[nxt]:
                visit[nxt] = True
                result += 1
                q.append(nxt)
    return result
answer = bfs(1)
print(answer)