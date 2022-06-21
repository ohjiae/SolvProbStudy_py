from collections import deque
import sys
input=sys.stdin.readline
visited=[0]*100001
record = [0] * 100001
n,k=map(int,input().split())


def bfs(visited):
    q=deque()
    q.append(n)
    while q:
        x=q.popleft()
        if x==k:
            break
        for i in (x-1,x+1,2*x):
            if 0<=i <=100000 and not visited[i]:
                record[i]=x
                visited[i]=visited[x]+1
                q.append(i)

bfs(visited) 

temp=k
answer=[k]
while temp!=n:
    answer.append(record[temp])
    temp=record[temp]
print(visited[k])
print(*answer[::-1])