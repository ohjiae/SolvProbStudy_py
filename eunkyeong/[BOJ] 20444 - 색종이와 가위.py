# 이분탐색 
n, k = map(int, input().split())
left = 0
right = n // 2
yn = False
while left <= right:
    row = (left + right) // 2
    col = n - row
    pieces = (row + 1) * (col + 1)
    if k == pieces:
        print('YES')
        yn = True
        break
    if k > pieces:
        left = row + 1
    else:
        right = row - 1
 
if not yn:
    print("NO")