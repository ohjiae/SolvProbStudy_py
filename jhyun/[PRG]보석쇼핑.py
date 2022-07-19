from collections import defaultdict
def solution(gems):
    km = defaultdict(int)
    answer = [0, 0]
    st, en, kind, min_kind = 0, 0, len(set(gems)), int(1e10)
    while True:
        if len(km) >= kind:
            km[gems[st]] -= 1
            if km[gems[st]] == 0:
                del(km[gems[st]])
            st += 1
        elif en == len(gems):
            break
        else:
            km[gems[en]] += 1
            en += 1

        if len(km) == kind:
            if min_kind > en - st:
                min_kind = en - st
                answer = [st + 1, en]
    return answer