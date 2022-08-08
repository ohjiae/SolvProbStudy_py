def solution(record):
    answer = []
    id = {rec.split()[1] : rec.split()[2] for rec in record if rec.split()[0] != 'Leave'}
    for i in record:
        state, usr = i.split()[0], i.split()[1]
        if state == 'Enter':
            answer.append(id[usr]+'님이 들어왔습니다.')
        elif state == 'Leave':
            answer.append(id[usr]+'님이 나갔습니다.')
    return answer