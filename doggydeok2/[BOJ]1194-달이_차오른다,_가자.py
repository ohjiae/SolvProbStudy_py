import collections


def escape(_x, _y):
    visited = [[[0] * M for _ in range(N)] for __ in range(64)]
    visited[0][_x][_y] = 1
    q = collections.deque([(_x, _y, 0)])
    while q:
        tx, ty, tkey = q.popleft()
        for k in range(4):
            nx, ny = tx + dij[k], ty + dij[k + 1]
            if 0 <= nx < N and 0 <= ny < M:
                if maze[nx][ny] == '#':
                    continue
                is_key = d_key.find(maze[nx][ny])
                if is_key != -1:
                    nkey = tkey | 2 ** is_key
                    if not visited[nkey][nx][ny]:
                        visited[nkey][nx][ny] = visited[tkey][tx][ty] + 1
                        q.append((nx, ny, nkey))
                    continue
                is_door = d_door.find(maze[nx][ny])
                if is_door != -1:
                    if tkey & 2 ** is_door and not visited[tkey][nx][ny]:
                        visited[tkey][nx][ny] = visited[tkey][tx][ty] + 1
                        q.append((nx, ny, tkey))
                    continue
                if maze[nx][ny] == '1':
                    return visited[tkey][tx][ty]
                # maze[nx][ny] == '0' or '.'
                if not visited[tkey][nx][ny]:
                    visited[tkey][nx][ny] = visited[tkey][tx][ty] + 1
                    q.append((nx, ny, tkey))
    return -1


dij = [0, -1, 0, 1, 0]
d_key, d_door = "abcdef", "ABCDEF"
N, M = map(int, input().split())
maze = []

sx = sy = 0
for i in range(N):
    maze.append(input())
    idx = maze[i].find('0')
    if idx != -1:
        sx, sy = i, idx
print(escape(sx, sy))
