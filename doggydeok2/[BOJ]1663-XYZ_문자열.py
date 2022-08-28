DP = [[0] * 4 for _ in range(101)]  # Len, X, Y, Z
DP[1][0] = DP[1][1] = DP[2][2] = DP[2][3] = DP[3][3] = DP[3][1] = 1
DP[2][0] = DP[3][0] = 2
dic = { 'X': 1, 'Y': 2, 'Z': 3 }

q, N = int(input()), int(input())
for i in range(4, N + 1):
    DP[i][1], DP[i][2], DP[i][3] = DP[i - 1][3], DP[i - 1][1], DP[i - 1][2] + DP[i - 1][1]
    DP[i][0] = DP[i][1] + DP[i][2] + DP[i][3]
if q == 1:
    print(DP[N][0])
elif q == 3:
    print(DP[N][dic[input()]])
else:
    k = int(input())
    while N > 3:
        if k > DP[N - 3][0]:
            k -= DP[N - 3][0]
            N -= 2
        else:
            N -= 3
    print('__XYZX'[N + k])
