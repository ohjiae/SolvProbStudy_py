#완전탐색 -> 투포인터
'''
처음부터 끝까지를 다 검토해야 하며 set(gems)의 원소를 다 가지고 있어야함
'''
#효율성 retry

def solution(gems):
    set_gems = set(gems)  # gems의 보석 종류
    len_gems = len(gems)  # gems의 길이
    answer = [0, len_gems - 1]
    start, end = 0, 0  # 투포인터 시작, 끝점

    while 0 <= start < len_gems and 0 <= end < len_gems:
        if set(gems[start:end + 1]) == set_gems:
            if (end - start + 1) < (answer[1] - answer[0] + 1):
                answer = [start, end]
            start += 1
        else:
            end += 1

    answer[0] += 1
    answer[1] += 1

    return answer