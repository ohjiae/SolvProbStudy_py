def dfs(now_row):
    global result
    if now_row == n :
        result += 1
    else :
        for q in range(n):
            rows[now_row] = q
            if chk(now_row):
                dfs(now_row + 1)

def chk(col):
    for now_col in range(col):
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
