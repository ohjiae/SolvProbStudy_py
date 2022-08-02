import bisect


T = int(input())
n, an = int(input()), list(map(int, input().split()))
m, bm = int(input()), list(map(int, input().split()))

a_acc, b_acc = [0] * n, [0] * m
a_acc[0], b_acc[0] = an[0], bm[0]
a_ables, b_ables = [an[0]], [bm[0]]
for i in range(1, n):
    a_acc[i] = a_acc[i - 1] + an[i]
    a_ables.append(a_acc[i])
    for j in range(i):
        a_ables.append(a_acc[i] - a_acc[j])
for i in range(1, m):
    b_acc[i] = b_acc[i - 1] + bm[i]
    b_ables.append(b_acc[i])
    for j in range(i):
        b_ables.append(b_acc[i] - b_acc[j])

a_ables.sort()
b_ables.sort()
cnt = 0
for a_able in a_ables:
    tg = T - a_able
    l_idx = bisect.bisect_left(b_ables, tg)
    if l_idx == len(b_ables):
        continue
    if b_ables[l_idx] == tg:
        r_idx = bisect.bisect_right(b_ables, tg)
        cnt += r_idx - l_idx
print(cnt)
