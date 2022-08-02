def check_correct(_str):
    _stack = []
    for _ch in _str:
        if _ch == '(':
            _stack.append(_ch)
        else:
            if not _stack:
                return False
            _stack.pop()
    return False if _stack else True


def make_correct(_str):
    if not _str:
        return _str
    
    u = v = ''
    cnt = 0
    for idx, ch in enumerate(_str):
        cnt += 1 if ch == '(' else -1
        if cnt == 0:
            u = _str[:idx + 1]
            v = _str[idx + 1:]
            break
    if not u:
        u, v = _str, ''
    
    if check_correct(u):
        return u + make_correct(v)
    # else
    temp = '(' + make_correct(v) + ')'
    reversed_u = ''
    for ch in u[1:-1]:
        reversed_u += ')' if ch == '(' else '('
    return temp + reversed_u
            
    
def solution(p):
    return make_correct(p)
            