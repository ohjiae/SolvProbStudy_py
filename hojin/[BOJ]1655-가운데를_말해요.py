import sys
import heapq
input=sys.stdin.readline

N=int(input())

lheap=[]
rheap=[]
for i in range(N):
    
    number=int(input())
    if len(lheap)==len(rheap):
        heapq.heappush(lheap,-number)
    else:
        heapq.heappush(rheap,number)
    if rheap and rheap[0] < -lheap[0]:
        leftValue = heapq.heappop(lheap)
        rightValue = heapq.heappop(rheap)
        heapq.heappush(lheap, -rightValue)
        heapq.heappush(rheap, -leftValue)
    print(-lheap[0])
    print(lheap,rheap)