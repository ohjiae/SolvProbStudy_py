import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    a,b=map(int,input().split())
    temp=0
    for i in range(a,b+1):
        num=i
        while num:
            num,mod=divmod(num,10)
            temp+=mod
    print(temp)