def brute_force(_info, _temp, _idx, _arrow):
    if _idx == 10 or _arrow == 0:
        _temp[10] += _arrow
        gap = get_score(_info, _temp)
        return [[-1]] if gap >= 0 else [_temp, -gap]

    not_get_best = brute_force(_info, _temp[:], _idx + 1, _arrow)
    get_best = [[-1]]
    if _arrow > _info[_idx]:
        _temp[_idx] = _info[_idx] + 1
        get_best = brute_force(_info, _temp[:], _idx + 1, _arrow - _info[_idx] - 1)

    if get_best[0][0] == -1:
        return not_get_best
    elif not_get_best[0][0] == -1:
        return get_best
    if not_get_best[1] == get_best[1]:
        for i in range(10, -1, -1):
            if not_get_best[0][i] == get_best[0][i]:
                continue
            return not_get_best if not_get_best[0][i] > get_best[0][i] else get_best
    return not_get_best if not_get_best[1] > get_best[1] else get_best


def get_score(_arr1, _arr2):
    gap = 0
    for i in range(10):
        gap += 10 - i if _arr1[i] >= _arr2[i] and _arr1[i] else i - 10 if _arr2[i] else 0
    return gap


def solution(n, info):
    return brute_force(info, [0] * 11, 0, n)


print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))
