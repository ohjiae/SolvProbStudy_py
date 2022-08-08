import sys
import heapq
input=sys.stdin.readline
n,m,x=map(int,input().split())
INF=int(1e9)
graph=[[] for i in range(n+1)]
temp=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
distance=temp.copy()
def dijsktra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

total_dist=[0]*n
#x에서 집으로 가는길
dijsktra(x)
for i in range(1,n+1):
    total_dist[i-1]+=distance[i]

#각 집에서 x 로 가는길
for i in range(1,n+1):
    distance=temp.copy()
    dijsktra(i)
    total_dist[i-1]+=distance[x]

print(max(total_dist))
    

