def check_able(results, s, tg):
    if s == 15:
        return sum(results) == 0
    for i in range(3):
        if results[s + i] and results[tg + 2 - i]:
            results[s + i] -= 1
            results[tg + 2 - i] -= 1
            if check_able(results, s if tg < 15 else s + 3, tg + 3 if tg < 15 else s + 6):
                return 1
            results[s + i] += 1
            results[tg + 2 - i] += 1
    return 0


print(*[check_able(list(map(int, input().split())), 0, 3) for _ in range(4)])
