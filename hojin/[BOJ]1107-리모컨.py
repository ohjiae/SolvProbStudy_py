import sys
input = sys.stdin.readline
target = int(input())
n = int(input())
if n:
    broken = set(input().split())
else:
    broken=set()

min_count = abs(100 - target)

for nums in range(1000001):
    for num in str(nums):
        if num in broken:
            break
    else:
            min_count = min(min_count, abs(nums - target) + len(str(nums)))

print(min_count)

