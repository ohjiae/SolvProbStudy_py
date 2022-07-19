def solution(gems):
    cnt_dict = {}
    for gem in set(gems):
        cnt_dict[gem] = 0
        
    lptr = rptr = jewel_types = 0
    ans = [1, len(gems)]
    while lptr <= rptr <= len(gems):
        if jewel_types == len(cnt_dict):
            if ans[1] - ans[0] + 1 > rptr - lptr:
                ans = [lptr + 1, rptr]
            cnt_dict[gems[lptr]] -= 1
            if cnt_dict[gems[lptr]] == 0:
                jewel_types -= 1
            lptr += 1
        else:
            if rptr == len(gems):
                break
            if cnt_dict[gems[rptr]] == 0:
                jewel_types += 1
            cnt_dict[gems[rptr]] += 1
            rptr += 1
            
    return ans
