import math
def solution(fees, records):
    time={}
    nums=[]
    for i in records:
        arr=list(i.split())
        num=arr[1]
        if num not in nums:
            nums.append(num)
    nums.sort()
    answer = [0]*len(nums)
    check=[False]*len(nums)
    time={x:0 for x in nums}
    for i in records:
        arr=list(i.split())
        h,m=map(int,arr[0].split(':'))
        mm=h*60+m
        if arr[2]=='IN':
            time[arr[1]]-=mm
            check[nums.index(arr[1])]=True
        elif arr[2]=='OUT':
            time[arr[1]]+=mm
            check[nums.index(arr[1])]=False
            
    for i in range(len(check)):
        if check[i]:
            time[nums[i]]+=23*60+59
            
    for i in range(len(nums)):
        if time[nums[i]]>fees[0]:
            fee=math.ceil((time[nums[i]]-fees[0])/fees[2])*fees[3]+fees[1]
            answer[i]=fee
        else:
            answer[i]=fees[1]
            
    return answer