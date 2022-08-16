from collections import defaultdict
N, K = map(int, input().split())

comb = defaultdict(set)
for i in range((N//2)+1):
    k = (i+1)*((N-i)+1)
    if k not in comb:
        comb[k].add((i,N-i))

print('YES' if K in comb else 'NO')