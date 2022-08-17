N = int(input())
solutions = sorted(list(map(int, input().split())))
l, r = 0, N - 1
nearest_zero = (abs(solutions[l] + solutions[r]), l, r)
while l < r:
    t_sum = solutions[l] + solutions[r]
    if nearest_zero[0] > abs(t_sum):
        nearest_zero = (abs(t_sum), l, r)
    if t_sum > 0:
        r -= 1
    else:
        l += 1
print(solutions[nearest_zero[1]], solutions[nearest_zero[2]])
