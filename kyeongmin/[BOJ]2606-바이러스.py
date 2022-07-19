node = int(input())
edge = int(input())
graph = [[] for _ in range(node +1)]
visited = [False] * len(graph)

for q in range(edge) :
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#print(graph)

count = 0
def dfs(graph, v, visited) :
    visited[v] = True
    global count
    count +=1 
    
    for i in graph[v] :
        if not visited[i] :
            dfs(graph,i,visited)
dfs(graph,1,visited)
print(count-1)