import sys
from sys import setrecursionlimit
setrecursionlimit(10**9)

def dfs(x,y):
    if days[y][x]<0:
        days[y][x]=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[y][x]<graph[ny][nx]:
                days[y][x]=max(days[y][x],dfs(nx,ny))
        days[y][x]+=1
    return days[y][x]

input=sys.stdin.readline
dx=[0,0,-1,1]
dy=[-1,1,0,0]

n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]
days=[[-1]*n for _ in range(n)]


answer=0

for i in range(n):
    for j in range(n):
        tmp=dfs(i,j)
        if answer<tmp:
            answer=tmp

print(answer)
