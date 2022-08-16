N, K = map(int, input().split())
left, right = 0, n//2+1
while left < right :
    mid = left+(right-left)//2
    cut = (mid-1)*(n-mid-1)
    if cut == K:
        print('YES')
        exit(0)
    elif cut < K:
        left = mid+1
    else :
        right = mid-1
print('NO')