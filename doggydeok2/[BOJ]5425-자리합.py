def get_digit_sum(_n):
    cnt_arr = [0] * 10
    if _n <= 0:
        return cnt_arr
    r, th = 0, 1
    while r != _n:
        n, r = divmod(_n, 10 ** th)
        d, dr = divmod(r, (10 ** (th - 1)))
        for num in range(10):
            cnt_arr[num] += (n + (num < d)) * (10 ** (th - 1)) + (dr + 1 if num == d else 0)
            # if num < d:
            #     cnt_arr[num] += (n + 1) * (10 ** (th - 1))
            # elif num == d:
            #     cnt_arr[num] += n * (10 ** (th - 1)) + dr + 1
            # else:
            #     cnt_arr[num] += n * (10 ** (th - 1))
        th += 1
    return cnt_arr


for tc in range(int(input())):
    a, b = map(int, input().split())
    a_nums, b_nums = get_digit_sum(a - 1), get_digit_sum(b)
    print(sum([(b_nums[i] - a_nums[i]) * i for i in range(10)]))
