from collections import deque
N, M, K = map(int, input().split())

arr = [list(map(int, input().rstrip())) for _ in range(N)] 
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
visited

dx = (-1,0,1,0)
dy = (0,1,0,-1)

# bfs 
def bfs():

    q = deque()
    q.append((0,0,0)) # x, y, k, depth
    # 처음 시작점
    visited[0][0][0] = 1
    while q:
        x,y,wall = q.popleft()
        # 맨 끝 점 도달
        if (x==N-1) & (y == M-1):
            return visited[N-1][M-1][wall]
        # 4방향
        for i in range(4):
            nx = x+dx[i]
            ny = x+dy[i]
            nw = wall+1
            # 밖으로 나가면 안됨 
            if (nx < 0) | (nx >= N) | (ny < 0) | (ny >= M):
                continue
            if visited[nx][ny][wall]:
                continue
            if arr[nx][ny] == 0:
                visited[nx][ny][wall] = visited[x][y][wall] + 1
                q.append((nx, ny, wall))
            if (arr[nx][ny] == 1) & (nw <= K):
                visited[nx][ny][wall] = visited[x][y][wall] + 1
                q.append((nx, ny, wall))
    return -1 


print(bfs())



