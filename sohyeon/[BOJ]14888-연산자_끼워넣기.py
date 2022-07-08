#브루트포스/백트래킹

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())  #+, -, *, /
answer = []

def func(add, sub, mul, div, res, i):

    if add == 0 and sub == 0 and mul == 0 and div == 0:     #모든 연산의 수가 0이되면 종료한다.
        answer.append(res)
        return

    if add > 0:     #덧셈
        func(add - 1, sub, mul, div, res + A[i], i + 1)
    if sub > 0:     #뺄셈
        func(add, sub - 1, mul, div, res - A[i], i + 1)
    if mul > 0:     #곱셈
        func(add, sub, mul - 1, div, res * A[i], i + 1)
    if div > 0:     #나눗셈
        if res > 0:
            func(add, sub, mul, div - 1, int(res / A[i]), i + 1)
        else:   #0보다 작은 경우: 양수로 만든 다음 -> 다시 음수로 바꿈
            func(add, sub, mul, div - 1, -int(abs(res) / A[i]), i + 1)

func(add, sub, mul, div, A[0], 1)
print(max(answer))
print(min(answer))