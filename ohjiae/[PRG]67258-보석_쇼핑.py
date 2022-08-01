def solution(gems):
    answer = [0,len(gems)]
    allgems = len(set(gems))
    left, right = 0,0
    gem_d = {gems[0]:1}
    while left < len(gems) and right < len(gems):

        if len(gem_d) == allgems:
            if right-left < answer[1]-answer[0]:
                answer = [left+1,right+1]
            else : # gem_d[gems[left]] -1 != 0:
                gem_d[gems[left]] -= 1
                if gem_d[gems[left]] == 0:
                    del gem_d[gems[left]]
                left += 1

        else:
            right += 1
            if right == len(gems) : break
            gem_d[gems[right]] = gem_d.get(gems[right], 0) + 1
    # print(answer)
    # print(f'gems={gems},gem_d={gem_d},l={left},r={right}')
    return answer

solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])