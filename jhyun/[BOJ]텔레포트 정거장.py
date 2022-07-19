from collections import deque, defaultdict
N, M = map(int, input().split())
S, E = map(int, input().split())
tp = defaultdict(list)
for _ in range(M):
    s, e = map(int, input().split())
    tp[s].append(e)
    tp[e].append(s)
def bfs():
    visit = [0] * (N + 1)
    visit[S] = 1
    q = deque([S])
    while q:
        cur = q.popleft()
        for nxt in tp[cur]:
            if visit[nxt] == 0:
                q.append(nxt)
                visit[nxt] = visit[cur] + 1
        if cur - 1 > 0 and visit[cur - 1] == 0:
            q.append(cur - 1)
            visit[cur - 1] = visit[cur] + 1
        if cur + 1 <= N and visit[cur + 1] == 0:
            q.append(cur + 1)
            visit[cur + 1] = visit[cur] + 1
    return visit[E] - 1
answer = bfs()
print(answer)