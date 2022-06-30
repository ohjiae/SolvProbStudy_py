N = int(input())

# Red, Green, Blue
normal_maps = []
normal_TF = [[False for _ in range(N)] for _ in range(N)] 

# Mixed, Blue
redgreen_maps = []
redgreen_TF = [[False for _ in range(N)] for _ in range(N)] 

#입력받는부분
for i in range(N) :
    temp = list(map(str,input()))
    normal_maps.append(temp)
import copy
redgreen_maps = copy.deepcopy(normal_maps)

# Mixed수정해주는 부분
for i in range(0,N) :
    for j in range(0, N) :
        if (normal_maps[i][j] == 'R') or (normal_maps[i][j] == 'G') :
            redgreen_maps[i][j] = 'W'


#BFS구성
from collections import deque
def bfs(y,x,what_map,what_TF) :
    
    Q = deque()
    Q.append((y,x))

    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    while Q :
        
        y,x = Q.popleft()
        what_TF[y][x] = True

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if nx<0 or nx>=N or ny<0 or ny>=N :
                continue 

            if what_map[ny][nx] != what_map[y][x] : #색깔이 다른 경우
                continue

            if what_TF[ny][nx] == True : #이미가봐서 True인경우
                continue 


            what_TF[ny][nx] = True #아직안가본곳을 True로설정,
            Q.append((ny,nx)) #다음 큐에 넣음

#Bfs를 얼마나 진입했는지 카운팅
normal_cnt = 0
redgreen_cnt = 0

#전체를 돌면서 (좌표,좌표,맵, TF) 를 넣어줌
#한번진행할때, 동일한 색상에 대해서 BFS를 진행, cnt+=1 진행
for i in range(N) :
    for j in range(N) :
        if (normal_TF[i][j]==False) : 
            bfs(i,j,normal_maps,normal_TF)
            normal_cnt +=1

        if (redgreen_TF[i][j]==False) : 
            bfs(i,j,redgreen_maps,redgreen_TF)
            redgreen_cnt +=1


print(normal_cnt)
print(redgreen_cnt)