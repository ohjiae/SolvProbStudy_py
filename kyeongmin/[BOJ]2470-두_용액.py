import sys
input = sys.stdin.readline
N = int(input())
numbers = list(map(int,input().split()))
numbers.sort()

#초기값 : 나올수있는 가장 큰 값
best_score = 1000000000 * 2
best_result = [0,0]
left_idx = 0
right_idx = N-1

#투포인터 
while left_idx != right_idx :

    hap = numbers[left_idx] + numbers[right_idx]

    #더 작아질수 있다면 
    if abs(best_score) > abs(hap) :
        best_score = hap

        best_result = numbers[left_idx], numbers[right_idx]

    #투포인터 이동
    if hap < 0 :
        left_idx += 1
    else :
        right_idx -= 1

print(*best_result)