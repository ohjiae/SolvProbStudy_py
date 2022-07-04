#bfs
import sys
from collections import deque
input = sys.stdin.readline

n ,k = map(int, input().split())
visited = [0 for i in range(100001)]
route = []

def bfs(v):
    queue = deque([v])

    while queue:
        v = queue.popleft()

        if v == k:
           return visited[v]

        for i in (v-1, v+1, 2*v):   #이동경로
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[v] + 1
                queue.append(i)
                

print(bfs(n))