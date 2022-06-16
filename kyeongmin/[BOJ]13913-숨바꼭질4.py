#testcase1
# N, K = 5, 17
#testcase2
# N, K = 0, 5

import sys
input = sys.stdin.readline
N, K = map(int, input().split())

MAX = 100001
visited = [-1] * MAX
moved = [-1] * MAX

from collections import deque
Q = deque()
Q.append(N)

visited[N] = 0 #방문처리
moved[N] = -1 #현재 값이 어디서 왔는지 기록

while Q :
    num = Q.popleft()

    #종료조건
    if num == K :
        break

    #진행조건
    else :
        for idx in (num-1, num+1, num*2) : #3가지 경우
            if (0<=idx<MAX) and (visited[idx] == -1) : #맵 밖을 벗어나지않고, 방문처리 한 경험이 없는거
                visited[idx] = 0
                moved[idx] = num
                Q.append(idx)

#초기값
i = moved[K]
result = [K]

#백트래킹
while True :

    #종료조건 #시작값에 도착했을떄
    if i == -1:
        # print(result)
        result.reverse()
        print(len(result) -1)
        print(*result)
        break

    #진행조건
    else :
        result.append(i)
        i = moved[i]
