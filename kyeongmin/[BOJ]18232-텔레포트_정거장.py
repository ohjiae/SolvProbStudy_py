# N, M = 10 ,3
# S, E = 2, 5
# graph = [[], [6, 3], [8], [1], [], [], [1], [], [2], [], []]
import sys 
input = sys.stdin.readline 
N, M = map(int, input().split())
S, E = map(int ,input().split())
graph = [ [] for _ in range(N+1)]
for _ in range(M) :
    x, y = map(int ,input().split())
    graph[x].append(y)
    graph[y].append(x)

from collections import deque 
Q = deque()
Q.append(S)

dp = [int(1e7) for _ in range(N+1)] #무지하게 큰 값으로 초기화 
dp[S] = 0 

while Q : 
    location = Q.popleft()

    #종료조건
    if location == E : 
        print(dp[location])
        break

    for i in [location+1, location-1] :
        if (1<=i<=N) and (dp[i] > dp[location]+1): 
            Q.append(i)
            dp[i] = dp[location]+1 

    if graph[location] :
        for i in graph[location] :
            if (dp[i] > dp[location]+1) :  
                Q.append(i)
                dp[i] = dp[location]+1
    # print(dp)