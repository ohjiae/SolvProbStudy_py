import sys
from collections import Counter
from collections import deque
input=sys.stdin.readline

def solution(p):
    if is_collect(p):
        return p
    return collect_convert(p)

def is_balanced(p):
    # counts=Counter(p)
    # return 1 if counts['(']==counts[')'] else 0
    return p.count('(') == p.count(')')

def is_collect(p):
    p=deque(p)
    cnt=0
    while(p):
        if p.popleft()=='(':
            cnt+=1
        else:
            cnt-=1
            if cnt<0:
                return 0
    return 1

def splituv(str):
    u, v = str, ""
    for i in range(2, len(str), 2):
        if is_balanced(str[:i]):
            u = str[:i]
            v = str[i:]
            break
    return u, v

def reverse_bracket(p):
    temp=""
    for s in p:
        if s=="(":
            temp+=")"
        else:
            temp+="("
    return temp

def collect_convert(p):
    #1
    if not p:
        return ''
    #2
    u,v=splituv(p)
    #3
    if is_collect(u):
        u+=collect_convert(v)
        return u
    else:
    #4
        #4-1
        temp="("
        #4-2
        temp+=collect_convert(v)
        #4-3
        temp+=")"
        #4-4
        u=reverse_bracket(u[1:-1])
        temp+=u
    return temp




p="()(())()"
print(solution(p))