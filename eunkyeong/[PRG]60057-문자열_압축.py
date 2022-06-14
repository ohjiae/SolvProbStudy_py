def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1): # 나눴을 때 최소 2묶음은 돼야됨
        compressed = ""
        prev = s[0:step]
        count = 1
        for j in range(step, len(s), step):
            # 이전 상태랑 동일하면 count 증가
            if prev == s[j:j+step]:
                count += 1
            else:
                if count >= 2:
                    compressed += str(count) + prev
                else: 
                    compressed += prev
                prev = s[j: j+step] # 상태 초기화 
                count = 1
        # 남아있는 문자열 
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 게 정답
        answer = min(answer, len(compressed))
    return answer