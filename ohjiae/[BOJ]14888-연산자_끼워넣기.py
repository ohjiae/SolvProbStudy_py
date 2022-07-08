from collections import deque
N = int(input())
arr = deque(map(int,input().split()))
pmsd = list(map(int,input().split()))
def m(arr, pmsd):
    while len(arr) != 1:
        fir = arr.popleft()
        sec = arr.popleft()
        thr = arr.popleft()
        a
        print(arr, fir, pmsd)

        arr.appendleft(fir)
    print(arr)
m(arr,pmsd)
