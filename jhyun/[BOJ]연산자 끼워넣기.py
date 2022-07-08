N = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split())) #+, -, x, /
min_v, max_v = int(1e10), -int(1e10)
def recur(idx, _sum):
    global op, min_v, max_v
    if idx == len(arr):
        min_v = min(_sum, min_v)
        max_v = max(_sum, max_v)
        return
    if op[0] > 0:
        op[0] -= 1
        recur(idx + 1, _sum + arr[idx])
        op[0] += 1
    if op[1] > 0:
        op[1] -= 1
        recur(idx + 1, _sum - arr[idx])
        op[1] += 1
    if op[2] > 0:
        op[2] -= 1
        recur(idx + 1, _sum * arr[idx])
        op[2] += 1
    if op[3] > 0:
        op[3] -= 1
        if _sum < 0:
            recur(idx + 1, -(abs(_sum) // arr[idx]))
        else:
            recur(idx + 1, _sum // arr[idx])
        op[3] += 1
recur(1, arr[0])
print(max_v, min_v, sep="\n")