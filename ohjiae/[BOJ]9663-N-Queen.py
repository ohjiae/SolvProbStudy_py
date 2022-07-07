def dfs(now_row):
    global result
    if now_row == n :
        result += 1
        print('done@',result)
    else :
        for q in range(n):
            rows[now_row] = q
            print('check row[지금행에]=퀸위치찾기','전체행=', rows, '지금행=', now_row, '퀸놓을 행=', q)
            if chk(now_row):
                dfs(now_row + 1)

def chk(col):
    for now_col in range(col):
        print('check rows[이전 열]=', col,'그리고 rows[지금열]=', now_col,'행전체=', rows, '행전체[이전열]=', rows[col], '행전체[지금열]=', rows[now_col])
        if rows[col] == rows[now_col]:
            return False
        if abs(rows[col] - rows[now_col]) == col-now_col :
            return False
    return True

n = int(input())
rows = [0] * n
result = 0
dfs(0)
print(result)