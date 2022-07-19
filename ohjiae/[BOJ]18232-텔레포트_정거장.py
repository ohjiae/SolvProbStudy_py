from sys import stdin
from collections import deque
input = stdin.readline
N, M = map(int,input().split())
S, E = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(node):
    q = deque()
    q.append((node,0))
    while q:
        now, d = q.popleft()
        if now == E :
            return d
        if 1 <= now <= N and not visited[now]:
                visited[now]= True
                q.append((now+1,d+1))
                q.append((now-1,d-1))
                if len(graph[now]) > 0:
                    for i in graph[now]:
                        q.append((i, d+1))
print(bfs(S))