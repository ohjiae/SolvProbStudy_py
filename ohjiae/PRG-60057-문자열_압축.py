def solution(s):
    answer = ''
    if len(s)==1:
        return 1
    else:
        def chk(s,x,answer):
            cut = len(s)//x
            now = s[:cut]
            cnt, start, end = 0, 0, cut
            while end <= len(s):
                if s[start:end] == now :
                    cnt += 1
                else:
                    if cnt == 1:
                        answer += now
                    else:
                        answer += str(cnt)+now
                    now = s[start:end]
                    print(f'cut={cut},cnt={cnt},s={start},e={end},ans {answer} + now {now} = {answer+now}')

                if len(s)-end < cut:
                    answer += s[end:]
                    break
                start = end
                end = end + cut
            return answer

        for i in range(2,len(s)):
            if len(s)//i == 1 :
                answer = s
                break
            else:
                chk(s,i,answer)
                if len(answer)>0:
                    break
        return answer