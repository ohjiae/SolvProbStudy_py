def solution(fees, records):
    answer = []
    return answer


## fees(list) : 기본시간, 기본요금, 단위시간, 단위요금 
fees = [180, 5000, 10, 600]	


import pandas as pd

## records(list) 
records
records = list(map(lambda x:x.split(), records))


record_df = pd.DataFrame(records) #[0].apply(lambda x:x.split())
record_t = record_df.groupby(1).agg(" ".join)
record_t

record_t[record_t[2].apply(lambda x:len(x.split(" "))) % 2 == 1].index[0]
record_df = record_df.append([['23:59', record_t[record_t[2].apply(lambda x:len(x.split(" "))) % 2 == 1].index[0], 'OUT']], ignore_index= True)
record_df
#record_df['time'] = 
#record_df = 
record_df.groupby(1).agg(" ".join)[0].apply(lambda x:time_cal(x)).apply(lambda x:money_cal(x)).tolist()
# if record_t[2].apply(lambda x:len(x.split(" "))).values % 2 == 1:
#     print(record_t)#record_t.append()


def time_cal(df):
    # in은 무조건 out 보다 앞선시간  
    # 시-분 분할 
    time_list = []
    df_split = df.split()
    for i, data in enumerate(df_split):
        if i % 2 == 0:
            hour = int(data.split(":")[0])
            min = int(data.split(":")[1])
        else:
            hour = int(data.split(":")[0]) - hour
            min = int(data.split(":")[1]) - min
            time_list.append(hour*60 + min)
            hour = 0
            min = 0
    return sum(time_list)

def money_cal(df):
    print(df)
    result = 0
    
    if df < fees[0]:
        result = (fees[1])
    else:
        ext_time = df - fees[0]
        a, b = divmod(ext_time, fees[2])
        if b > 0:   
            result = (fees[1] + (a+1) * fees[3])
        else:
            result = (fees[1] + a * fees[3])
    return result



## 시간초과 
# 1. 차량별 누적 주차 시간 계산 (출차 - 입차, 기록 안된 경우 23:59)
from itertools import groupby
#sort 필요 
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

records = list(map(lambda x:list(x.split(" ")), sorted(records, key = lambda x:x.split()[1])))
records
group = groupby(records, lambda x:x[1])

cum_time = []
list_items[:][:]

for key, items in group:
    list_items = list(items)
    if len(list_items) % 2 == 1:
        list_items.append(['23:59', key, 'OUT'])

    times = []
    for i, data in enumerate(list_items):
        print(data)
        if i % 2 == 0:
            hour = int(data[0].split(":")[0])
            min = int(data[0].split(":")[1])
        else:
            hour = int(data[0].split(":")[0]) - hour
            min = int(data[0].split(":")[1]) - min
            times.append(hour*60 + min)
            hour = 0
            min = 0
        print(times)
    cum_time.append(sum(times))
cum_time

    # # list_items[1::2] : 홀수 
    # for j,i in zip(list_items[1::2], list_items[0::2]):
    #     hour =  abs(int(j[0].split(":")[0]) - int(i[0].split(":")[0]))
    #     min = abs(int(j[0].split(":")[1]) - int(i[0].split(":")[1]))
    #     times.append(hour*60 + min)
    # print(times) # - 
    # cum_time.append(sum(times))
    
# 2. 차량 요금 계산 
fees = [180, 5000, 10, 600]
money_cal(cum_time)



def money_cal(df):
    result = []
    for i in df:
        if i < fees[0]:
            result.append(fees[1])
        else:
            ext_time = i - fees[0]
            a, b = divmod(ext_time, fees[2])
            if b > 0:   
                result.append(fees[1] + (a+1) * fees[3])
            else:
                result.append(fees[1] + a * fees[3])
    return result

