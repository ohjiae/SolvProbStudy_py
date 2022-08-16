from sys import stdin
from collections import deque
input = stdin.readline

N, M = map(int, input().split())
move = [0, -1, 0, 1, 0]
graph = [list(map(int,input().split())) for _ in range(M)]

def bfs():
    q = deque()
    q.append((0,0))
    vst = [[0]*M for _ in range(N)]
    vst[0][0] = 1
    leftCZ = 0
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + move[d]
            ny = y + move[d+1]
            if 0 <= nx < N and 0 <= ny < M and not vst[nx][ny]:
                if graph[nx][ny] == 0 :
                    q.append((nx,ny))
                    vst[nx][ny] = 1
                elif graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    vst[nx][ny] = 1
                    leftCZ += 1
    return leftCZ
res = []
time = 0
while True:
    CZS = bfs()
    if CZS == 0 :
        print(time)
        print(res[-1])
        break
    time += 1
    res.append(CZS)