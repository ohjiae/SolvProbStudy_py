import sys
import heapq
input=sys.stdin.readline
n=int(input())
univs=[list(map(int,input().split())) for _ in range(n)]

temp=set()
answer=0
heap=[]
univs=sorted(univs,key=lambda x: (x[1],-x[0]))
for p,d in univs:
    heapq.heappush(heap,p)
    if len(heap)>d:
        heapq.heappop(heap)

print(sum(heap))