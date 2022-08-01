from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
frd = [[] for _ in range(N)]
vst = [False] * N
for i in range(M):
    a, b = map(int,input().split())
    frd[a].append(b)
    frd[b].append(a)
flag = False
def dfs(idx, cnt):
    global flag
    vst[idx] = True
    if cnt > 3 :
        flag = True
        return
    for i in frd[idx]:
        if not vst[i]:
            dfs(i,cnt+1)
            vst[i] = False

for f in range(N):
    dfs(f,0)
    vst[f] = False
    if flag : break

print(1 if flag else 0)