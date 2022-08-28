import heapq


N = int(input())
homeworks = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[0], -x[1]))
targets = [0]

for deadline, cups in homeworks:
    if deadline <= len(targets):
        if targets[0] >= cups:
            continue
        heapq.heappop(targets)
    heapq.heappush(targets, cups)

print(sum(targets))
