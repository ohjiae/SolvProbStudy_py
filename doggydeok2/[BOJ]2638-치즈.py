from collections import deque


def bfs(x, y, t):
    q = deque([(x, y)])
    while q:
        tx, ty = q.popleft()
        for k in range(4):
            nx, ny = tx + dij[k], ty + dij[k + 1]
            if 0 <= nx < N and 0 <= ny < M and plate[nx][ny] == 0 and visited[nx][ny] == -1:
                q.append((nx, ny))
                visited[nx][ny] = t


def is_meltable(x, y, t):
    cnt = 0
    for k in range(4):
        nx, ny = x + dij[k], y + dij[k + 1]
        if 0 <= nx < N and 0 <= ny < M and plate[nx][ny] == 0 and visited[nx][ny] != -1 and visited[nx][ny] != t:
            cnt += 1
    return cnt >= 2


dij = [0, -1, 0, 1, 0]
N, M = map(int, input().split())
plate = [list(map(int, input().split())) for _ in range(N)]

visited = [[-1] * M for _ in range(N)]
bfs(0, 0, 0)

flag, time = True, 1
while flag:
    flag = False
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if plate[i][j] == 1 and is_meltable(i, j, time):
                flag = True
                plate[i][j] = 0
                visited[i][j] = time
                bfs(i, j, time)
    time += 1
print(time - 2)