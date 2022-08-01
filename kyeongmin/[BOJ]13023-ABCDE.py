import sys 

N, M = map(int, input().split())
friends = [[] for _ in range(N)]
for _ in range(M) :
    t1, t2  = map(int ,input().split())
    friends[t1].append(t2)
    friends[t2].append(t1)

def dfs(idx, dep) :
    if dep == 4 :
        print("1")
        sys.exit(0)

    for i in friends[idx] :
        if visit[i] == False :
            visit[i] = True 
            dfs(i, dep+1)
            visit[i] = False 

for v in range(N) :
    visit = [False for _ in range(N)]
    visit[v] = True 
    result = dfs(v,0)

print("0")