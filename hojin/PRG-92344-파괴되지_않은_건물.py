# def solution(board, skill):
#     answer = 0
#     for sk in skill:
#         type, r1, c1, r2, c2,degree=sk
#         if type==1:
#             degree*=-1
            
#         for i in range(r1,r2+1):
#             for j in range(c1,c2+1):
#                 board[i][j]+=degree
#     for i in board:
#         for j in i:
#             if j>=1:
#                 answer+=1

#     return answer


def solution(board, skill):
    answer = 0
    n = len(board); m = len(board[0])
    skills=[[0] * (len(board[0])+1) for _ in range(len(board)+1)]
    
    
    for sk in skill:
        type, r1, c1, r2, c2,degree=sk
        if type==1:
            degree*=-1
        skills[r1][c1]+=degree
        skills[r1][c2+1]-=degree
        skills[r2+1][c1]-=degree
        skills[r2+1][c2+1]+=degree

    
    for i in range(len(skills)):
        for j in range(1,len(skills[0])):
            skills[i][j]+=skills[i][j-1]
            
    for i in range(1,len(skills)):
        for j in range(len(skills[0])):
            skills[i][j]+=skills[i-1][j]
    

    
    answer=0
    for r in range(len(board)):
        for c in range(len(board[0])):
            if skills[r][c] + board[r][c] > 0:
                answer += 1
    return answer