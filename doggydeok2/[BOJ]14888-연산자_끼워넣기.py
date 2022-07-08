def ops_order(n, r):
    global maxR, minR
    if n == N:
        if maxR < r:
            maxR = r
        if minR > r:
            minR = r
    else:
        if ops[0]:
            ops[0] -= 1
            ops_order(n + 1, r + nums[n])
            ops[0] += 1
        if ops[1]:
            ops[1] -= 1
            ops_order(n + 1, r - nums[n])
            ops[1] += 1
        if ops[2]:
            ops[2] -= 1
            ops_order(n + 1, r * nums[n])
            ops[2] += 1
        if ops[3]:
            ops[3] -= 1
            ops_order(n + 1, r // nums[n] if r >= 0 else -(-r // nums[n]))
            ops[3] += 1


N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))  # 합 차 곱 분
maxR, minR = -1000000000, 1000000000

ops_order(1, nums[0])
print(maxR)
print(minR)