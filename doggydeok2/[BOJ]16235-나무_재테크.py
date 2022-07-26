import sys
rl = sys.stdin.readline


dij = [1, 0, -1, 0, 1, -1, -1, 1, 1]  # 8방향
N, M, K = map(int, rl().split())
winter_injection = [[0] * (N + 1)] + [[0] + list(map(int, rl().split())) for _ in range(N)]
nutrients = [[0] * (N + 1)] + [[0] + [5] * N for _ in range(N)]
trees = [[[] for _ in range(N + 1)] for __ in range(N + 1)]

for _ in range(M):
    x, y, z = map(int, rl().split())
    trees[x][y].append(z)

for _ in range(K):
    # Spring
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            trees[i][j].sort()
            for idx, tree in enumerate(trees[i][j]):
                if nutrients[i][j] >= tree:
                    nutrients[i][j] -= tree
                    trees[i][j][idx] += 1
                else:  # Summer
                    nutrients[i][j] += sum([dead >> 1 for dead in trees[i][j][idx:]])
                    trees[i][j] = trees[i][j][:idx]
                    break
    # Fall
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # Winter
            nutrients[i][j] += winter_injection[i][j]
            for tree in trees[i][j]:
                if tree % 5:
                    continue
                for k in range(8):
                    ni, nj = i + dij[k], j + dij[k + 1]
                    if 1 <= ni <= N and 1 <= nj <= N:
                        trees[ni][nj].append(1)
print(sum([sum(len(tree) for tree in alive) for alive in trees]))
