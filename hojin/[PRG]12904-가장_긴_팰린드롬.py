def check(number):
    if number==number[::-1]:
        return True
    else:
         return False


def solution(s):
    answer = 0
    length=len(s)
    for i in range(length):
        for j in range(i+1,length+1):
            if check(s[i:j]):
                if answer<len(s[i:j]):
                    answer=len(s[i:j])
    return answer