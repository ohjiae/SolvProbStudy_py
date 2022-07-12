from collections import deque
import sys
rl = sys.stdin.readline


def bfs():
    q = deque([[0, 0]])
    while q:
        tidx, ty = q.popleft()
        tx = adl[ty][tidx]
        for i in range(max(0, ty - 2), min(ty + 3, T + 1)):
            for idx, nx in enumerate(adl[i]):
                if -2 <= tx - nx <= 2 and visited[i][idx] == -1:
                    visited[i][idx] = visited[ty][tidx] + 1
                    if i == T:
                        return visited[i][idx]
                    q.append([idx, i])
    return -1


n, T = map(int, rl().split())
adl = [[] for _ in range(T + 1)]
visited = [[] for _ in range(T + 1)]
adl[0].append(0)
visited[0].append(0)
for _ in range(n):
    x, y = map(int, rl().split())
    adl[y].append(x)
    visited[y].append(-1)
print(bfs())