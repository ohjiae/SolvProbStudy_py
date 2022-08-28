INF = 16000
N, M = map(int, input().split())
friends = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    friends[a][b] = friends[b][a] = 1

for i in range(1, N + 1):
    friends[i][i] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            friends[i][j] = min(friends[i][j], friends[i][k] + friends[k][j])

min_kb = INF * 127
min_kb_idx = -1
for idx, val in enumerate([sum(row) for row in friends]):
    if min_kb > val:
        min_kb_idx = idx
        min_kb = val

print(min_kb_idx)
