def cutable():
    n, k = map(int, input().split())
    l, r = 0, n // 2
    while l <= r <= n:
        m = (l + r) // 2
        cuts = (m + 1) * (n - m + 1)
        if k == cuts:
            return 'YES'
        if k > cuts:
            l = m + 1
        else:
            r = m - 1
    return 'NO'


print(cutable())
