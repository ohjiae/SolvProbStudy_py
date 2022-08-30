import sys
rl = sys.stdin.readline


def find_parent(_x):
    if _x != parents[_x]:
        parents[_x] = find_parent(parents[_x])
    return parents[_x]


N, M = int(rl()), int(rl())
parents = [i for i in range(N + 1)]
costs = []
for _ in range(M):
    a, b, c = map(int, rl().split())
    costs.append([c, a, b])
costs.sort()
min_cost = 0
for c, a, b in costs:
    pa, pb = find_parent(a), find_parent(b)
    if pa == pb:
        continue
    elif pa < pb:
        min_cost += c
        parents[pb] = pa
    else:
        min_cost += c
        parents[pa] = pb
print(min_cost)
