# N = 6
# datas = [1, 2, 3, 4, 5, 6]
# arrs = [2, 1, 1, 1]

import sys 
input = sys.stdin.readline 

N = int(input().strip())
datas = list(map(int , input().split()))
arrs = list(map(int , input().split()))

something = ['+','-','*','/']
strs = ""
for i,j in zip(arrs, something) :
    strs += (j*i)

from itertools import permutations
temps = list(permutations(strs))
max_result = -999999999
min_result = 999999999

for temp in temps : 
    result = datas[0]
    for data in zip ( datas[1:],temp) : 
        if data[1] == '+' :
            result += data[0]
        elif data[1] == '-' :
            result -= data[0]
        elif data[1] == '*' :
            result *= data[0]
        else : 
            if result >= 0 :
                result //= data[0]
            else : 
                result = (result*(-1) // data[0]) *(-1)
    max_result = max(max_result,result)
    min_result = min(min_result,result)

print(max_result)
print(min_result)