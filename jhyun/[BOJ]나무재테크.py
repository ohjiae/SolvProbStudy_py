import heapq as hq
answer = 0
N, M, K = map(int, input().split())
s2d2 = [list(map(int, input().split())) for _ in range(N)]
nutrients = [[5] * N for _ in range(N)]
trees = [[[] for i in range(N)] for j in range(N)]
dr = [1, 0, -1, 0, 1, 1, -1, -1]
dc = [0, 1, 0, -1, 1, -1, 1, -1]
def in_range(r, c):
    return 0 <= r < N and 0 <= c < N
def spring_and_summer():
    global nutrients, trees
    #봄은 나이가 적은 나무부터 양분을 먹음
    #여름은 나무가 먹을 양분이 없으면 죽어서 나이 / 2값이 양분에 추가
    for r in range(N):
        for c in range(N):
            for _ in range(len(trees[r][c])):
                tree_age = hq.heappop(trees[r][c])
                if tree_age <= nutrients[r][c]:
                    nutrients[r][c] -= tree_age
                    hq.heappush(trees[r][c], tree_age + 1)
                else:
                    nutrients[r][c] += tree_age // 2
def fall():
    for r in range(N):
        for c in range(N):
            for tree_age in trees[r][c]:
                if tree_age % 5 == 0:
                    for i in range(8):
                        nr = r + dr[i]
                        nc = c + dc[i]
                        if not in_range(nr, nc):
                            continue
                        hq.heappush(trees[nr][nc], 1)
def winter():
    for i in range(N):
        for j in range(N):
            nutrients[i][j] += s2d2[i][j]
for _ in range(M):
    r, c, age = map(int, input().split())
    hq.heappush(trees[r - 1][c - 1], age)
for _ in range(K):
    spring_and_summer()
    fall()
    winter()
for r in range(N):
    for c in range(N):
        answer += len(trees[r][c])
print(answer)