import sys
input= sys.stdin.readline

N,C=map(int,input().split())

plots=sorted([int(input()) for _ in range(N)])

dist=0
s=1
e=plots[-1]-plots[0]

while s<=e:
    m=(s+e)//2
    current=plots[0]
    cnt=1

    for i in range(1,N):
        if plots[i]>=current+m:
            cnt+=1
            current=plots[i]
    if cnt>=C:
        s=m+1
        dist=m
    else:
        e=m-1


print(dist)