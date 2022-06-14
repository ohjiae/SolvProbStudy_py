def solution(n):
    nums = [1,2,4]
    t = 1
    answer = ''
    if n < 4: answer=str(nums[n-1])
    else:
        while n > 3:
            n -= 1
            res = divmod(n,3)
            n = res[0]
            answer = str(nums[res[1]]) + answer
            if n <= 3:
                answer = str(nums[res[0]-1]) + answer
    return answer