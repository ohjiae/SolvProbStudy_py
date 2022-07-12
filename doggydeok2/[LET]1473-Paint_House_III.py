class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # DP[group][color][idx] = cost
        DP = [[[int(1e7)] * m for _ in range(n)] for __ in range(target + 1)]
        if houses[0] == 0:
            for j in range(n):
                DP[1][j][0] = cost[0][j]
        else:
            DP[1][houses[0] - 1][0] = 0
            
        for i in range(1, m):
            for k in range(1, target + 1):
                if houses[i] == 0:
                    for j in range(n):
                        DP[k][j][i] = min(DP[k][j][i - 1] + cost[i][j], DP[k][j][i])
                        for tj in range(n):
                            if tj == j:
                                continue
                            DP[k][j][i] = min(DP[k][j][i], DP[k - 1][tj][i - 1] + cost[i][j])
                elif houses[i] == houses[i - 1]:
                    DP[k][houses[i] - 1][i] = DP[k][houses[i] - 1][i - 1]
                else:
                    DP[k][houses[i] - 1][i] = DP[k][houses[i] - 1][i - 1]
                    for tj in range(n):
                        if tj == houses[i] - 1:
                            continue
                        DP[k][houses[i] - 1][i] = min(DP[k][houses[i] - 1][i], DP[k - 1][tj][i - 1])

        ans = min([DP[target][j][-1] for j in range(n)])
        return -1 if ans == int(1e7) else ans
        