N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
# DP[idx][initial_color][color] = cost
DP = [[[1e8] * 3 for __ in range(3)] for _ in range(N)]
DP[0][0][0], DP[0][1][1], DP[0][2][2] = costs[0][0], costs[0][1], costs[0][2]
for i in range(1, N):
    for j in range(3):
        DP[i][j][0] = min(DP[i - 1][j][1], DP[i - 1][j][2]) + costs[i][0]
        DP[i][j][1] = min(DP[i - 1][j][2], DP[i - 1][j][0]) + costs[i][1]
        DP[i][j][2] = min(DP[i - 1][j][0], DP[i - 1][j][1]) + costs[i][2]
DP[-1][0][0] = DP[-1][1][1] = DP[-1][2][2] = 1e8
print(min([min(costs) for costs in DP[-1]]))
