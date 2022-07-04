#dp + dfs
'''
*point: DP에 현재 노드(now)부터 DFS를 진행했을 때, 최대로 움직일 수 있는 칸이 몇인지 기록한다. -> 메모이제이션
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


n = int(input().rstrip())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if dp[x][y] == -1:
        dp[x][y] = 0    #dfs에서 첫 방문하는 지점을 0으로 초기화한다


        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > board[x][y]: #더 큰 값이 있는지 비교
                dp[x][y] = max(dp[x][y], dfs(nx, ny))   #있으면 현재값과 비교해 더 큰 값을 취한다

    return dp[x][y] + 1


result = 0
for j in range(n):
    for k in range(n):
        result = max(result, dfs(j, k))

print(result)