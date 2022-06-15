def solution(board, skill):
    answer = 0


    M, N = len(board[0]), len(board)
    tile = [[0 for _ in range(M+1)] for _ in range(N+1)]

    #이차원 누적합을 사용할거라 점찍기 과정
    #시작점, [r2+1][c2+1] 에는 더해주고
    #[r1][c2+1], [r2+1][c1] 에는 빼줄건데 ( 누적합에서 값 상쇄하기위함)
    for type, r1, c1, r2, c2, degree in skill :
        if type == 1 :
            tile[r1][c1] += (-degree)
            tile[r2+1][c2+1] += (-degree)
            tile[r1][c2+1] -= (-degree)
            tile[r2+1][c1] -= (-degree)
        else :
            tile[r1][c1] += degree
            tile[r2 + 1][c2 + 1] += degree
            tile[r1][c2+1] -= degree
            tile[r2+1][c1] -= degree

    #가로 누적합
    for j in range(0,N+1) :
        for i in range(1,M+1) :
            tile[j][i] += tile[j][i-1]

    #세로 누적합
    for i in range(0,M+1) :
        for j in range(1,N+1) :
            tile[j][i] += tile[j-1][i]

    for j in range(N) :
        for i in range(M) :
            if board[j][i] + tile[j][i] > 0 :
                answer += 1
    
    
    return answer