# di = [-1, 1, -1, 1]
# dj = [-1, -1, 1, 1]

# 체스판에 퀸을 놓고 8방향을 다 확인하는 방법 (171428 KB, 28188 ms)
def n_queen(n):
    if n == N:
        global cnt
        cnt += 1
    else:
        for m in range(N):
            if not xis[m] and checking(m, n):
                v[n][m] = xis[m] = 1
                n_queen(n + 1)
                v[n][m] = xis[m] = 0


def checking(x, y):
    # for w in range(1, N):
        # for k in range(4):
        #     cal_y, cal_x = y + w * dj[k], x + w * di[k]
        #     if 0 <= cal_y < N and 0 <= cal_x < N and v[cal_y][cal_x]: return 0
    for k in range(1, min(N - y, N - x)):
        if v[y + k][x + k]: return 0
    for k in range(1, min(N - y, x + 1)):
        if v[y + k][x - k]: return 0
    for k in range(1, min(y + 1, N - x)):
        if v[y - k][x + k]: return 0
    for k in range(1, min(y + 1, x + 1)):
        if v[y - k][x - k]: return 0
    return 1


N = int(input())
v = [[0] * N for _ in range(N)]
xis = [0] * N
cnt = 0

for j in range(N):
    v[0][j] = xis[j] = 1
    n_queen(1)
    v[0][j] = xis[j] = 0

print(cnt)


# 열 및 두 각 대각선 방향의 배열 사용한 방법 (132808 KB, 6664 ms)
# def n_queen(n):
#     global cnt
#     if n == N: cnt += 1
#     else:
#         for m in range(N):
#             if not (xis[m] or rulb[m + n] or lurb[N - 1 + n - m]):
#                 xis[m] = rulb[m + n] = lurb[N - 1 + n - m] = 1
#                 n_queen(n + 1)
#                 xis[m] = rulb[m + n] = lurb[N - 1 + n - m] = 0


# N = int(input())
# xis, rulb, lurb = [0] * N, [0] * (2 * N - 1), [0] * (2 * N - 1)
# cnt = 0
# n_queen(0)
# print(cnt)