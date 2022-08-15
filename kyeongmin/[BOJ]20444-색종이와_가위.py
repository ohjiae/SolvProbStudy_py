import sys 
input = sys.stdin.readline 

#data input 
N, K  = map(int, input().split())
start, end = 0, N//2

flag = False 
while start <= end :

    mid = (start + end) //2 #mid = 가로로 자른횟수
    val = (mid+1) * ((N-mid)+1) #N-mid=세로로 자른횟수
    #val = 가로로자른횟수+1 * 세로로자른횟수+1

    if val > K :
        end = mid - 1
    elif val < K :
        start = start + 1
    else :
        flag = True 
        break

if flag == True :
    print("YES")
else : 
    print("NO")