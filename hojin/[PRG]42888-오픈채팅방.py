def solution(record):
    newrec=[]
    name={}
    answer=[]
    for _ in record:
        temp=_.split()
        
        if temp[0] == "Enter":
            newrec.append(temp[1])
            name[temp[1]]=temp[2]
    
        elif temp[0]== "Leave":
            newrec.append('-'+temp[1])
            
        elif temp[0]== "Change":
            name[temp[1]]=temp[2]
    # print(newrec)
    for rec in newrec:
        if rec[0]=='-':
            answer.append(name[rec[1:]]+"님이 나갔습니다.")
        else:
            answer.append(name[rec]+"님이 들어왔습니다.")
    return answer

