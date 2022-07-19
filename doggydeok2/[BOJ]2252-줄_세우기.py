import collections


N, M = map(int, input().split())
taller_list = [[] for _ in range(N + 1)]
topologies = [0] * (N + 1)

for i in range(M):
    A, B = map(int, input().split())
    taller_list[A].append(B)
    topologies[B] += 1

q = collections.deque([])
for i in range(1, N + 1):
    if topologies[i] == 0:
        q.append(i)

ans = [0] * N
ptr = 0
while q:
    ans[ptr] = temp = q.popleft()
    ptr += 1
    for taller in taller_list[temp]:
        topologies[taller] -= 1
        if topologies[taller] == 0:
            q.append(taller)

print(*ans)
