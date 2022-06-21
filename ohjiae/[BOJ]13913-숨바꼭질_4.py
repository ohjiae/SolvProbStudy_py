from collections import deque
N, K = map(int, input().split())
T = [0]*100001
way = [0]*100001

def history(x):
    tmp = []
    here = x
    for _ in range(T[x]+1):
        tmp.append(here)
        here = way[here]
    print(' '.join(map(str, tmp[::-1])))

def bfs():
    q=deque([N])
    while q:
        now = q.popleft()
        if now == K:
            print(way[now])
            history(now)
            return now
        for i in [now+1,now-1,now*2]:
            if 0<=i<=100000 and T[i]==0:
                q.append(i)
                T[i] = T[now]+1
                way[i] = now
bfs()