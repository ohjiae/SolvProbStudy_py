from collections import defaultdict
import heapq as hq
N = int(input())
sm = defaultdict(set)
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
answer = 0
arr = []
def in_range(r, c):
    return 0 <= r < N and 0 <= c < N
for _ in range(N ** 2):
    student, *temp = map(int, input().split())
    sm[student] = set(temp)
    arr.append(student)
result = [[0] * N for _ in range(N)]
for n in arr:
    q = []
    for r in range(N):
        for c in range(N):
            like = 0
            empty = 0
            if result[r][c] != 0:
                continue
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not in_range(nr, nc):
                   continue
                if result[nr][nc] in sm[n]: #좋아하는 학생
                    like += 1
                if result[nr][nc] == 0:
                    empty += 1
            hq.heappush(q, (-like, -empty, r, c))
    _, _, row, col = hq.heappop(q)
    result[row][col] = n
for r in range(N):
    for c in range(N):
        pw = 0
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not in_range(nr, nc):
                continue
            if result[nr][nc] in sm[result[r][c]]:
                pw += 1
        answer += 0 if pw == 0 else 10 ** (pw - 1)
print(answer)