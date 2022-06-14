def solution(board, skill):
    answer = 0
    arr=[[0]*(len(board[0])+1) for i in range(len(board)+1)]
    
    for i in skill:
        t,r1,c1,r2,c2,degree=i
        if t==1:
            arr[r1][c1]-=degree
            arr[r1][c2+1]+=degree
            arr[r2+1][c1]+=degree
            arr[r2+1][c2+1]-=degree
        else:
            arr[r1][c1]+=degree
            arr[r1][c2+1]-=degree
            arr[r2+1][c1]-=degree
            arr[r2+1][c2+1]+=degree
            
    for i in range(len(board)):
        for j in range(len(board[0])):
            arr[i][j+1]+=arr[i][j]
            
    for i in range(len(board[0])):
        for j in range(len(board)):
            arr[j+1][i]+=arr[j][i]
            
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j]+=arr[i][j]
            if board[i][j]>0:
                answer+=1
    return answer