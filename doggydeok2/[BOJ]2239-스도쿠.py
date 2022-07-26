def fill_sudoku(sx, sy, cnt):
    if cnt == 81:
        return True
    for y in range(sy, 9):
        for x in range(9):
            if sudoku[y][x] == 0:
                for n in range(1, 10):
                    if not row_check[y][n] and not cal_check[x][n] and not block_check[3 * (y // 3) + (x // 3)][n]:
                        row_check[y][n] = cal_check[x][n] = block_check[3 * (y // 3) + (x // 3)][n] = True
                        sudoku[y][x] = n
                        if fill_sudoku(x, y, cnt + 1):
                            return True
                        row_check[y][n] = cal_check[x][n] = block_check[3 * (y // 3) + (x // 3)][n] = False
                        sudoku[y][x] = 0
                return False


sudoku = [[int(n) for n in input()] for _ in range(9)]
row_check = [[False] * 10 for _ in range(9)]
cal_check = [[False] * 10 for _ in range(9)]
block_check = [[False] * 10 for _ in range(9)]
fill = 0

for i in range(9):
    for j in range(9):
        if sudoku[i][j] != 0:
            row_check[i][sudoku[i][j]] = True
            cal_check[j][sudoku[i][j]] = True
            block_check[3 * (i // 3) + (j // 3)][sudoku[i][j]] = True
            fill += 1

if fill_sudoku(0, 0, fill):
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end='')
        print()
