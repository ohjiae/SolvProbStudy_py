from collections import deque
N, K = map(int, input().split())
T = 0
q = deque(N)
done = {}
fast = [False for _  in range(K+2)]
while q:
    now = q.popleft()
    if now == K :
        print(T)
        print()
    else:
        done[now+1] = T
        done[now-1] = T
        done[now*2] = T
