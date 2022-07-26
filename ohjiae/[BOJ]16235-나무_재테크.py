from collections import deque
from sys import stdin
import math
input = stdin.readline
N,M,years =  map(int,input().split())
S2D2 = [list(map(int,input().split())) for _ in range(N)]
trees = deque()
for _ in range(M):
    x,y,age = map(int,input().split())
    trees.append((x-1,y-1,age))
ground = [[5]*N for _ in range(N)]
dir = [(-1,-1),(-1,0),(-1,+1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def seasons(trees):
    dead = []
    # 봄 : 나이만큼 양분 먹고 나이 1 증가, 어린나무부터 먹기 양분 못먹으면 죽음
    # 가을 : 나무 번식, if 나무 나이%5==0 : 여덟방향 나이1 나무가 범위안에서 생성
    for i in range(len(trees)):
        x,y,age = map(int,trees.popleft())
        if age > ground[x][y]:
            dead.append((x,y,age))
        else:
            ground[x][y] -= age
            trees.append((x,y,age+1))

    # 여름 : 봄에 죽은 나무 -> 양분으로. 땅 += 나이//2 소수점 아래 버림
    while dead :
        dt = dead.pop()
        ground[dt[0]][dt[1]] += math.trunc(dt[2]//2)

    for i in range(len(trees)):
        x,y,age = trees[i][0], trees[i][1], trees[i][2]
        if age % 5 == 0:
            for d in dir:
                if 0 <= x + d[0] < N and 0 <= y + d[1] < N:
                    trees.append((x + d[0], y + d[1], 1))
    return trees

for y in range(years):
    seasons(trees)
    if y != years-1:
        # 겨울 : s2d2가 땅에 돌아다니며 양분 추가
        for gx in range(N):
            for gy in range(N):
                ground[gx][gy] += S2D2[gx][gy]
print(len(trees))