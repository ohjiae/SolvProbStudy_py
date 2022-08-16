N, M = int(input()), int(input())
more_heavy = [[] for _ in range(N + 1)]
more_light = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    more_light[A].append(B)
    more_heavy[B].append(A)

can_check = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    can_check[i][i] = 1

for i in range(1, N + 1):
    heavier, lighter = [i], [i]
    for comp in heavier:
        for heavy in more_heavy[comp]:
            if can_check[i][heavy] == 0:
                can_check[i][heavy] = 1
                heavier.append(heavy)

    for comp in lighter:
        for light in more_light[comp]:
            if can_check[i][light] == 0:
                can_check[i][light] = 1
                lighter.append(light)

for i in range(1, N + 1):
    print(can_check[i].count(0) - 1)
