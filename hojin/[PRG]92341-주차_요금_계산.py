from math import ceil
def timetomin(time):
    return int(time[:2])*60+int(time[3:])

def calprice(record,fees):
    temp=[]
    for x in record:
        time=sum(x[1])
        if time<=fees[0]:
            temp.append(fees[1])
        else:
            temp.append(fees[1]+ ceil((time-fees[0])/fees[2])*fees[3])
    return temp
def solution(fees, records):
    in_time={}
    stay_time={}
    for record in records:
        time,number,state=record.split(" ")
        if state=="IN":
            in_time[number]=timetomin(time)
        else:
            if number not in stay_time.keys():
                stay_time[number]=[]
            stay_time[number].append(timetomin(time)-in_time[number])
            del in_time[number]

    if in_time:
        for x in in_time:
            if x not in stay_time.keys():
                stay_time[x]=[]
            stay_time[x].append(timetomin("23:59")-in_time[x])
    stay_time=sorted(stay_time.items())

    answer = (calprice(stay_time,fees))
    
    return answer