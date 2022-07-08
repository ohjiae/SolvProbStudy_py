#n-quene problem/dfs+백트래킹
'''
*퀸은 8방향으로 거리 상관없이 움직일 수 있다.
-> 따라서 퀸은 1줄에 1개 밖에 못 놓는다.

*퀸이 같은 열에 존재하거나 같은 대각선에 존재하는지를 확인하여
존재하지 않는다면 퀸을 놓음으로써 경우의 수를 늘려간다.

*python 시초, pypy 통과
'''

import sys
input = sys.stdin.readline

n = int(input())
queen = [0] * n     #퀸의 위치를 넣을 1차원 배열 생성
result = 0

def adj(idx):
    for i in range(idx):
        if queen[idx] == queen[i] or abs(queen[idx] - queen[i]) == idx - i:
            return False
    return True


def dfs(idx):
    global result

    if idx == n:
        result += 1
        return

    for i in range(n):
        queen[idx] = i
        if adj(idx):
            dfs(idx + 1)

dfs(0)
print(result)