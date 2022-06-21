from collections import deque
import sys


def rotate(board,L):
    len_ice=len(board)
    new_board=[[0]*len_ice for _ in range(len_ice)]
    leap=2**L
    for y in range(0,len_ice,leap):
        for x in range(0,len_ice,leap):
            for i in range(leap): # 열 인덱스
                for j in range(leap): # 행 인덱스
                    new_board[y + j][x + leap - i - 1] = board[y + i][x + j]
    return new_board

def count_remove(board):
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    len_ice=len(board)
    cnts=[[0]*len_ice for _ in range(len_ice)]
    for y in range(len_ice):
        for x in range(len_ice):
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<len_ice and 0<=ny<len_ice and board[ny][nx]>0:
                    cnts[y][x]+=1 

    for y in range(len_ice):
        for x in range(len_ice):
            if cnts[y][x] < 3:
                if board[y][x]>=1:
                    board[y][x] -= 1
                
    return board

def find_chunk(board):

    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    len_ice=len(board)
    

    visited=[[False]*len_ice for _ in range(len_ice)]
    n_ice=0
    answer=0
    for y in range(len_ice):
        for x in range(len_ice):
            cnt=0
            if visited[y][x] or board[y][x]==0:
                continue
            
            q=deque()
            q.append((y,x))
            visited[y][x]=True

            while q:
                sy,sx=q.popleft()
                n_ice+=board[sy][sx]
                cnt+=1
                
                for i in range(4):
                    nx=sx+dx[i]
                    ny=sy+dy[i]
                    if nx<0 or ny<0 or nx>=len_ice or ny>=len_ice or visited[ny][nx]:
                        continue
                    if board[ny][nx]!=0:
                        visited[ny][nx]=True
                        q.append((ny,nx))

            answer=max(answer,cnt)
    return answer,n_ice

input= sys.stdin.readline

n,q=map(int,input().split())
iceboard=[]


for i in range(2**n):
    iceboard.append(list(map(int,input().split())))
len_ice=len(iceboard)
Ls=list(map(int,input().split()))

new_iceboard=rotate(iceboard,Ls[0])
new_iceboard=count_remove(new_iceboard)

for l in Ls[1:]:
    new_iceboard=rotate(new_iceboard,l)
    new_iceboard=count_remove(new_iceboard)



chunk,n_ice=find_chunk(new_iceboard)

print(n_ice)
print(chunk)





# [[0, 0, 2, 4, 1, 2, 3, 3] 
#  [8, 7, 4, 4, 7, 7, 6, 3], 
#  [1, 2, 2, 2, 1, 1, 1, 4], 
#  [8, 6, 6, 5, 8, 5, 5, 5], 
#  [5, 5, 5, 8, 5, 6, 6, 8], 
#  [4, 1, 1, 1, 2, 2, 2, 1], 
#  [3, 6, 7, 7, 4, 4, 7, 8], 
#  [3, 3, 2, 1, 4, 2, 0, 0]]

