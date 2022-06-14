def solution(s):
    answer =  1000
    if len(s)==1:
        return 1
    for i in range(1,len(s)//2+1):
        temp=''
        cnt=1
        a=s[:i]
        for j in range(i,len(s),i):
            if s[j:j+i]==a:
                cnt+=1
            else:
                if cnt==1:
                    temp+=a
                else:
                    temp+=str(cnt)+a
                a=s[j:i+j]
                cnt=1
        if cnt==1:
            temp+=a
        else:
            temp+=str(cnt)+a
        answer=min(answer, len(temp))
    return answer