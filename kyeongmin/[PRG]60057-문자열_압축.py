def solution(s):
    def splited_function() :
        temp = []
        i,j = 0, spliter

        while j < (N+1):
            temp.append( s[i:j])
            i += spliter
            j += spliter

        #겹쳐지지않는 단어에 대한 예외처리
        if i != N :
            temp.append(s[i:N])
        return temp

    def counting_function() :
        result_temp = ""
        word_temp = temp[0]
        cnt = 1

        idx = 1

        while True:
            if word_temp == temp[idx]:
                cnt += 1

            else:
                if cnt == 1:
                    result_temp = result_temp + word_temp
                else:
                    result_temp = result_temp + str(cnt) + word_temp
                word_temp = temp[idx]
                cnt = 1

            idx += 1
            if idx == len(temp):
                break

        # 마지막꺼는 안더해져있어서 예외처리
        if cnt == 1:
            result_temp = result_temp + word_temp
        else:
            result_temp = result_temp + str(cnt) + word_temp

        return result_temp

    #answer = 0
    answer = 1000
    N = len(s)
    
    if N == 1 :
        answer = 1
    else :

        for spliter in range(1, N//2 +1,1) :

            temp = splited_function()
            result_temp = counting_function()

            answer = min(len(result_temp), answer)
            # print(answer)
        # print(answer)

    
    
    return answer