def solution(record):
    user = {}
    logs = []
    for row in record:
        row_parse = list(row.split())
        if row_parse[0] == 'Enter':
            inout, uid, username = row.split()
            user[uid] = username
            logs.append((uid, 1))
        elif row_parse[0] == 'Leave':
            inout, uid = row.split()
            logs.append((uid, 0))
        else:
            inout, uid, username = row.split()
            user[uid] = username
    
    ans = []
    for log in logs:
        uid, inout = log
        ans.append(f'{user[uid]}님이 {"들어왔습니다" if inout else "나갔습니다"}.')
        
    return ans