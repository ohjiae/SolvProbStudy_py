import sys
from collections import deque 
input = sys.stdin.readline 

#INIT 
N, M = map(int ,input().split())
tile = []
for _ in range(N) :
    tile.append(list(map(int, input().split())))
visit = [[False for _ in range(M)] for _ in range(N)]
counting = [[0 for _ in range(M)] for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


#어떤치즈를 없에는지 카운팅하는 함수
def cheese_bfs(y_init,x_init) :
    Q = deque()
    Q.append([y_init, x_init])
    visit[y_init][x_init] = True 

    while Q :
        y, x = Q.popleft()

        for i in range(4) :
            ddy = y + dy[i]
            ddx = x + dx[i]

            #맵 밖을 나가면 안됨 
            if ((0<=ddy<N) and (0<=ddx<M)) and (visit[ddy][ddx]==False) :
                
                #치즈라면 -> 큐에 안넣고, 카운팅만 올린다
                if tile[ddy][ddx] == 1 :
                    counting[ddy][ddx] += 1
                #치즈가 아니면 -> 큐에 넣고, 방문처리를 한다
                else :
                    visit[ddy][ddx] = True 
                    Q.append([ddy,ddx])


# 2이상을 찾아서 -> 치즈를 제거 
def find_2(y_init, x_init) :
    for i in range(N) :
        for j in range(M) :
            if counting[i][j] >= 2 :
                tile[i][j] = 0

#누적된 visit, counting을 초기화 시켜주는 함수 
def init_function() :
    visit = [[False for _ in range(M)] for _ in range(N)]
    counting = [[0 for _ in range(M)] for _ in range(N)]
    return visit, counting 

#만약 치즈가 남아있다면 return True, 아니면 return False 
def end_function(N,M):
    for i in range(N) :
        for j in range(M) :
            if tile[i][j] == 1:
                return True 
    return False


#MAIN 
days = 0 
while True :
    if(end_function(N,M)) == False :
        break

    days += 1
    visit, counting = init_function()
    cheese_bfs(0,0)
    find_2(0,0)

print(days)

