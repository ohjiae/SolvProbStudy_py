from collections import deque

n, k = map(int, input().split())
seconds = [0] * 100001  # 위치를 방문할 때 걸리는 시간
visited = [0] * 100001  # 위치 방문 기록

def move(now):
    route = []  # 이동 경로
    loc = now   # 현재 위치(역으로 경로 찾기)
    for _ in range(seconds[now] + 1):
        route.append(loc)   # 현재 위치
        loc = visited[loc]  # 전의 위치
    print(' '.join(map(str, route[::-1])))  # 거꾸로 출력


def bfs():
    q = deque()
    q.append(n)
    while q:
        now = q.popleft()
        if now == k:  # 수빈이가 동생을 만났을 때
            print(seconds[now])  # 시간 출력
            move(now)  # 이동 경로 출력
            return
        for next in (now-1, now+1, now*2):  # 이동할 수 있는 방향 3가지
            if 0<=next<=100000 and seconds[next] == 0:
                seconds[next] = seconds[now] + 1  # 이동할 위치에 시간입력
                q.append(next)  # 이동할 위치 추가
                visited[next] = now  # 현재 이동위치 기록

bfs()
