import bisect


N, K = map(int, input().split())
satisfactions = [0] + list(map(int, input().split()))
accumulates = [0] * (N + 1)
for i in range(N + 1):
    accumulates[i] = accumulates[i - 1] + satisfactions[i]
DP = [0] * (N + 1)

for idx, satisfaction in enumerate(satisfactions):
    DP[idx] = DP[idx - 1]
    finish_here_idx = bisect.bisect_left(accumulates, accumulates[idx - 1] - K + 1, 0, idx)
    DP[idx] = max(DP[idx], DP[finish_here_idx] + accumulates[idx] - accumulates[finish_here_idx] - K)
print(DP[-1])
