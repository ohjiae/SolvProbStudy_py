def solution(s):
    for i in range(len(s),0,-1):
        for j in range(0,len(s)-i+1):
            str=s[j:j+i]
            if str[::-1]==str:
                return len(str)