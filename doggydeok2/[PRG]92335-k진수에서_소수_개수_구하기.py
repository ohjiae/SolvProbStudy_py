def dec_to_k(_n, _k):
    division = []
    while _n:
        division.append(str(_n % _k))
        _n //= _k
    return ''.join(division[::-1])


def is_prime(_n):
    if _n < 2:
        return 0
    for n in range(2, int(_n ** 0.5) + 1):
        if _n % n == 0:
            return 0
    return 1


def solution(n, k):
    kth = dec_to_k(n, k)
    ans = 0
    for num in kth.split('0'):
        if not num:
            continue
        ans += is_prime(int(num))
    return ans