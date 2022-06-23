from collections import deque

def bfs(x,y):
    visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque()
    q.append([x,y,K])   # K : 뚫을 수 있는 벽의 수
    visited[x][y][K] = 1
    while q:
        x,y,cnt = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][cnt]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if maps[nx][ny] and cnt > 0 and visited[nx][ny][cnt-1] == 0:
                    visited[nx][ny][cnt-1] = visited[x][y][cnt]+1
                    q.append([nx,ny,cnt-1])
                elif maps[nx][ny] == 0 and visited[nx][ny][cnt] == 0:
                    visited[nx][ny][cnt] = visited[x][y][cnt]+1
                    q.append([nx,ny,cnt])

    return -1

N, M, K = map(int, input().split())
maps = [list(map(int, input().strip())) for _ in range(N)]

print(bfs(0,0))