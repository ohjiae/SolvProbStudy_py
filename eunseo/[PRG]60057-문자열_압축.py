def solution(s):
    length = []
    if len(s) == 1:
        return 1

    for idx in range(1, len(s) // 2 + 1):
        result = ''
        cnt = 1
        halfStr = s[:idx]
        for i in range(idx, len(s), idx):
            if s[i:i + idx] == halfStr:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ''
                result += str(cnt) + halfStr
                halfStr = s[i:i + idx]
                cnt = 1

        if cnt == 1:
            cnt = ''
        result += str(cnt) + halfStr
        length.append(len(result))

    return min(length)
