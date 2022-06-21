def solution(s):
    answer = 1
    l = len(s)
    save = [0] * (l + 2)
    if l > 3:
        stt, end = 0, 2
        pin = 1
        while pin != l:
            if 0 <= stt <= l and 0 <= end <= l + 2:
                if s[stt] == s[end]:
                    save[pin] += 2
                    stt -= 1
                    end += 1
                    for i in save[stt:end+1]:
                        save[i] = save[pin]
                    print('here',save)
                else:
                    pin += 1
                    stt = pin - 1
                    end = pin + 1
                    print('22',save)
            else:
                pin += 1
                stt = pin - 1
                end = pin + 1
                print('33',save)

    else:
        if not l:
            return 0
        elif s[0] != s[-1]:
            return 1
        else:
            return 2
    # return answer
solution("abcdcba")