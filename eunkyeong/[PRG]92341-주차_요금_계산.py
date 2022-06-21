s = "abacde"
s

## 시간초과 
def ispalindrome(x):
    if x == x[::-1]:
        return len(x)

def solution(s):
    answer = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if ispalindrome(s[i:j]):
                answer = max(answer, ispalindrome(s[i:j])) 
    return answer
solution(s)

## 통과 
def isPalindrome(x):
    if x==x[::-1]:
        return True
def solution(s):
    answer=0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if isPalindrome(s[i:j]):
                if answer<len(s[i:j]):
                    answer=len(s[i:j])
    return answer
