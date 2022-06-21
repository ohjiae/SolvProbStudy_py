import math
def solution(fees, records):
    answer = {}
    park = {}
    for rec in records:
        carnum = rec[6:10]
        mins = int(rec[:2]) * 60 + int(rec[3:5])
        if carnum in park:
            if carnum in answer:
                answer[carnum] += mins - park[carnum]
            else:
                answer[carnum] = mins - park[carnum]
            del park[carnum]
        else:
            park[carnum] = mins

    while park:
        left = park.popitem()
        if left[0] in answer:
            answer[left[0]] += 1439 - left[1]
        else:
            answer[left[0]] = 1439 - left[1]

    for car in answer:
        if answer[car] <= fees[0]:
            answer[car] = fees[1]
        else:
            overfees = math.ceil((int(answer[car]) - fees[0]) / fees[2]) * fees[3]
            answer[car] = fees[1] + overfees

    return [v for k, v in sorted(answer.items())]