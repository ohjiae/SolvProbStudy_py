import sys
import heapq
INF=int(10e9)
input=sys.stdin.readline
n,m,k=map(int,input().split())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

distance=[[INF]*(k+1) for _ in range(n+1)]
for i in range(k + 1):
    distance[1][i] = 0


def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start,0))
    while q:
        dist, now, p = heapq.heappop(q)
        if distance[now][p] < dist:
            continue
        #포장이 가능한 경우
        if p + 1 <= k:
            for (next, next_dist) in graph[now]:
                if distance[next][p + 1] > dist:
                    distance[next][p + 1] = dist
                    heapq.heappush(q, (dist, next, p + 1))

        #포장을 하지 않는 경우
        for (next, next_dist) in graph[now]:
            if distance[next][p] > dist + next_dist:
                distance[next][p] = dist + next_dist
                heapq.heappush(q, (dist + next_dist, next, p))


dijkstra(1)
ans = INF
for i in range(k + 1):
    ans = min(ans, distance[n][i])

print(ans)