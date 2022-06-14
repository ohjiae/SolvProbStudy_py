## 몫 // 나머지 % 
n = 13
first = n // 3
first

if n % 3 == 1:
    last = '1'
elif n % 3 == 2:
    last = '2'
else:
    last = '4'
    first -= 1

if first % 3 == 0: # 3의 배수 > 4로 변경
    first = 4

rem = []

n = 15

answer = ''
while n > 0:
    n, mod = divmod(n, 3)
    if mod == 0:
        n -= 1
    answer += str(mod)
    answer = answer[::-1]


answer
answer.replace('0', '4')





    if answer[-1] == '0':
        answer[-1] = '4'

answer


    rem.append(n % 3)
    n = n //3
answer[:-1]



rem
rem.reverse()
if rem[-1] == 0:
    rem[:-1] - 1 
rem
    

def get124(n, lists):
    a, b = divmod(n, 3) # 124
    if a == 0:
        return lists
    else:
        return get124(a, lists)

n = 6
answer = []
answer = get124(n, answer)
answer.sort(reverse=True)
answer



print(str(first)+ last)