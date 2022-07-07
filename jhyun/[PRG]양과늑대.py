from collections import deque
#양 노드를 최대로 방문한 개수
def bfs(start: int, visit, graph, info) -> int:
    #이전 노드의 방문상태, 현재 노드, 양, 늑대
    q = deque([(0b1, 0, 1, 0)])
    visit[0][0b1] = True
    result = 0
    while q:
        cur_stat, cur, cur_sheep, cur_wolf = q.popleft()
        result = max(result, cur_sheep)
        for nxt in graph[cur]:
            nxt_stat = cur_stat | (1 << nxt)
            nxt_sheep = cur_sheep if cur_stat & (1 << nxt) else cur_sheep + (info[nxt] + 1) % 2
            nxt_wolf = cur_wolf if cur_stat & (1 << nxt) else cur_wolf + info[nxt]
            if nxt_wolf >= nxt_sheep: continue
            if not visit[nxt][nxt_stat]:
                visit[nxt][nxt_stat] = True
                q.append((nxt_stat, nxt, nxt_sheep, nxt_wolf))
    return result
def solution(info, edges):
    visit = [[False] * (1 << len(info)) for _ in range(len(info))]
    graph = [[] for _ in range(len(info))]
    for edge in edges:
        st, en = edge
        graph[st].append(en)
        graph[en].append(st)
    answer = bfs(0, visit, graph, info)
    return answer