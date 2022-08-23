original_maps = []
N, M = map(int,input().split())

for i in range(N) :
    original_maps.append(   list( map(int,input().split()) ) )



#원래 맵을 넣고 딥카피
import copy
maps = copy.deepcopy(original_maps)

#bfs구현
from collections import deque
def bfs(y,x) :

    Q = deque()
    Q.append((y,x))

    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    while Q :
        y,x = Q.popleft() 

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=M or ny<0 or ny>=N : #맵 밖으로 벗어나면 
                continue 

            if maps[ny][nx] == 1 : # 벽인경우
                continue 
            
            if maps[ny][nx] == 0 : # 빈칸이여서
                maps[ny][nx] = 2 #바이러스가 퍼지는경우
                Q.append((ny,nx)) 
        


#0을 모두 찾는과정 : 빈칸을 모두 찾아야, 랜덤으로 3개의 벽을 지음
maps_0 = []
for i in range(N):
    for j in range(M) :
        if maps[i][j] == 0 :
            maps_0.append((i,j))


#임의로 0이 있는곳에 3개를 뽑아내는거
from itertools import combinations
new_zeros = list(combinations(maps_0,3))
res_zero = [] 

# 여기서부터 돌기 시작함
for index1 in new_zeros :
    maps = copy.deepcopy(original_maps)
    for index2 in index1 : #랜덤으로 3개의 벽을 짓고
        y, x = index2 #그곳의 좌표를 확인
        maps[y][x] = 1 #좌표에 임의의 벽을 짓기


    #bfs돌기 
    for i in range(N) :
        for j in range(M) :
            if maps[i][j] == 2: #만약 바이러스를 만난다면 BFS진행
                bfs(i,j )

    #0의 갯수세기
    cnt = 0 
    for i in range(N) :
        for j in range(M) :
            if maps[i][j] == 0 :
                cnt += 1
    res_zero.append(cnt) 

#최대 0의 갯수를 출력
print(max(res_zero))