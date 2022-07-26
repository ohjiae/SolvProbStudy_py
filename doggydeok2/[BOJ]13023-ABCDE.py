import sys
rl = sys.stdin.readline


def dfs_five_depth(_n, _depth):
    if _depth == 5:
        return True
    for friend in friends[_n]:
        if not visited[friend]:
            visited[friend] = 1
            if dfs_five_depth(friend, _depth + 1):
                return True
            visited[friend] = 0
    return False


def find_ans():
    for i in range(N):
        visited[i] = 1
        if dfs_five_depth(i, 1):
            return 1
        visited[i] = 0
    return 0


N, M = map(int, rl().split())
friends = [[] for _ in range(N)]
visited = [0] * N
for _ in range(M):
    s, e = map(int, rl().split())
    friends[s].append(e)
    friends[e].append(s)

print(find_ans())
