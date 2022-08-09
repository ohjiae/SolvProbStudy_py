def solution(gems):
    gem_dict = {}
    gem_num = len(set(gems))
    start, end = 0, 0
    
    gem_dict[gems[0]] = 1
    answer = [0, len(gems)]
    
    while True:
        while True:
            if gem_dict[gems[start]] > 1: 
                gem_dict[gems[start]] -= 1
                start += 1
            else: break
        
        if len(gem_dict) == gem_num and \
            (end - start) < (answer[1] - answer[0]):
            answer = [start + 1, end + 1]
        
        end += 1
        if end == len(gems): return answer
            
        if gems[end] in gem_dict: 
            gem_dict[gems[end]] += 1
        else: 
            gem_dict[gems[end]] = 1
    
    return [start + 1, end + 1]