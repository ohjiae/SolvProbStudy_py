def find_order_recursion(n, val, up, left, down, right):
    if n == 0:
        return val
    segment = (2 ** (n - 1)) ** 2
    mid_y, mid_x = (up + down) // 2, (left + right) // 2
    if mid_y <= r:
        up = mid_y
        val += 2 * segment
    else:
        down = mid_y
    if mid_x <= c:
        left = mid_x
        val += segment
    else:
        right = mid_x
    return find_order_recursion(n - 1, val, up, left, down, right)


N, r, c = map(int, input().split())
print(find_order_recursion(N, 0, 0, 0, 2 ** N, 2 ** N))
