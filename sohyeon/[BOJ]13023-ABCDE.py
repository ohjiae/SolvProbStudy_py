#simulation -> dfs 그래프 탐색
'''
5명의 친구가 연결고리로 이어져있는지 확인하는 문제
-> *point: 깊이가 4 이상인 그래프인지 확인하는 문제이다.
'''

import sys
input = sys.stdin.readline

#간선에 가중치가 없는 그래프를 인접리스트 방식으로 구현
n, m = map(int, input().split())    #사람의수(노드), 관계의수(엣지)

visited = [False] * (n+1)
fin = False

relation = [[] for i in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)


def dfs(idx, depth):
    global fin

    visited[idx] = True

    if depth == 4:  #친구 관계가 4 이상 연결되어있다면,
        print(1)    #1 출력하고
        exit()      #빠져나옴

    for i in relation[idx]:     #친구관계 확인
        if not visited[i]:      #탐색하지 않은 친구라면
            dfs(i, depth+1)
            visited[i] = False   # dfs에서 빠져나왔다는건 제일 안쪽까지 파고들었다가 다시 나오는 것이기 때문에 방문표시를 풀어줌/ 백트래킹을 통해 깊이 확인


for i in range(n):  #각 친구들의 친구관계를 확인
    dfs(i, 0)
    visited[i] = False


if fin:
    print(1)
else:
    print(0)