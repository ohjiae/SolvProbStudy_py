# BFS
N, K = map(int, input().split())
dist = [0] * 100001
move = [0] * 100001

from collections import deque

def path(x):
    arr =[]
    temp = x
    for _ in range(dist[x]+1):
        arr.append(temp)
        temp = move[temp]
    print(' '.join(map(str, arr[::-1])))

def bfs():
    q = deque()
    q.append(N)

    while q:
        x = q.popleft() # depth 0 에서는 5꺼내고... 
        # x 가 K(동생위치)가 됐을 때  return 
        # 된 case path만 arr에 담는 함수 path
        if x == K:
            print(dist[x])
            path(x)
            return x 
        
        # for문으로 계속 위치 업데이트 
        for i in (x+1, x-1, 2*x):
            if 0 <= i <= 100000 and dist[i] == 0:
                q.append(i)
                dist[i] = dist[x] + 1
                move[i] = x

bfs()

