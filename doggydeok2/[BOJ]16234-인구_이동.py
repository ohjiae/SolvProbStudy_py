import collections


def bfs(y, x):
    for ty, tx in group_dict[union_cnt]:
        for k in range(4):
            ny, nx = ty + dij[k], tx + dij[k + 1]
            if 0 <= ny < N and 0 <= nx < N and \
                    L <= abs(populations[ny][nx] - populations[ty][tx]) <= R and \
                    not visited[ny][nx]:
                group_dict[union_cnt].append((ny, nx))
                sum_dict[union_cnt] += populations[ny][nx]
                visited[ny][nx] = union_cnt


dij = [0, -1, 0, 1, 0]
N, L, R = map(int, input().split())
populations = [list(map(int, input().split())) for _ in range(N)]
day = 0

while True:
    visited = [[0] * N for _ in range(N)]
    group_dict = collections.defaultdict(list)
    sum_dict = collections.defaultdict(int)
    union_cnt = 0
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                union_cnt += 1
                visited[r][c] = union_cnt
                group_dict[union_cnt].append((r, c))
                sum_dict[union_cnt] += populations[r][c]
                bfs(r, c)

    if union_cnt < N * N:
        day += 1
        for i in range(1, union_cnt + 1):
            for r, c in group_dict[i]:
                populations[r][c] = sum_dict[i] // len(group_dict[i])
    else:
        break

print(day)
