from collections import deque
import sys
rl = sys.stdin.readline


N, M = map(int, rl().split())
adl = [[i - 1, i + 1] for i in range(N + 1)]
adl[N].pop()
S, E = map(int, rl().split())

for _ in range(M):
    a, b = map(int, rl().split())
    adl[a].append(b)
    adl[b].append(a)

q = deque([S])
visited = [-1] * (N + 1)
visited[S] = visited[0] = 0
while q and visited[E] == -1:
    tx = q.popleft()
    for nxt in adl[tx]:
        if visited[nxt] == -1:
            q.append(nxt)
            visited[nxt] = visited[tx] + 1
print(visited[E])
