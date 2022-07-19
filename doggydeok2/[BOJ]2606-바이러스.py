def find_parent(x):
    if x != computer[x]:
        computer[x] = find_parent(computer[x])
    return computer[x]


def grouping(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x > y:
        computer[x] = y
    else:
        computer[y] = x


N, E = int(input()), int(input())
computer = [i for i in range(N + 1)]

for i in range(E):
    a, b = map(int, input().split())
    grouping(a, b)

for i in range(1, N + 1):
    computer[i] = find_parent(i)

print(computer.count(1) - 1)
