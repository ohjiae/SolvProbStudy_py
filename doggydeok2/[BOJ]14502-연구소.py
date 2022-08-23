from collections import deque


def bfs(_stage):
    q = deque(viruses[:])
    while q:
        tx, ty = q.popleft()
        for k in range(4):
            nx, ny = tx + dij[k], ty + dij[k + 1]
            if 0 <= nx < N and 0 <= ny < M and _stage[nx][ny] == 0:
                _stage[nx][ny] = 2
                q.append((nx, ny))
    return sum([_stage[i].count(0) for i in range(N)])


def brute_force(_x, _y, _k):
    if _k == 3:
        return bfs([data[i][:] for i in range(N)])
    else:
        cnt_max = 0
        for i in range(_x, N):
            for j in range(_y if i == _x else 0, M):
                if data[i][j] == 0:
                    data[i][j] = 1
                    cnt_max = max(cnt_max, brute_force(i, j, _k + 1))
                    data[i][j] = 0
        return cnt_max


def get_virus():
    arr = []
    for i in range(N):
        for j in range(M):
            if data[i][j] == 2:
                arr.append((i, j))
    return arr


dij = [0, -1, 0, 1, 0]
N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
viruses = get_virus()
print(brute_force(0, 0, 0))
