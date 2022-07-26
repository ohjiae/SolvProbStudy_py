puzzles = []
x = [set() for _ in range(9)]
y = [set() for _ in range(9)]
z = [set() for _ in range(9)]

def z_pos(x,y):
    nz = (nx//3, ny//3)
    if not nz[0]:
        return nz[1]
    elif nz[0] == 1:
        return nz[1]+3
    else:
        return nz[1]+6

# 맵 채우면서 가진 숫자 체크
for nx in range(9):
    l = list(input())
    puzzles.append(l)
    for ny in range(9):
        l[ny] = int(l[ny])
        if l[ny]:
            x[nx].add(l[ny])
            y[ny].add(l[ny])
            nz = z_pos(nx, ny)
            z[nz].add(l[ny])


def find_num(row,col,now):
    numlist = ({1,2,3,4,5,6,7,8,9} if now == 0 else now)
    numlist -= x[row]
    numlist -= y[col]
    part = z_pos(row,col)
    numlist -= z[part]

    if len(numlist) == 1:
        n = numlist.pop()
        x[nx].add(n)
        y[ny].add(n)
        nz = z_pos(nx, ny)
        z[nz].add(n)
        return n
    else :
        return numlist

# x,y,z중 가장 긴 원소를 가진 리스트 찾기
# def find_long():
#     xyz = [('x',max(x,key=len)),('y',max(y,key=len)),('z',max(z,key=len))]
#     xyz.sort(key= lambda x: len(x[1]),reverse=True)
#     return xyz[0][0]

done = [False]*3
while not all(done):

    for nx in range(9):
        for ny in range(9):
            now = puzzles[nx][ny]
            if now == 0 or type(now) == set:
                puzzles[nx][ny] = find_num(nx, ny, now)

    if not done[0] and len(min(x,key=len)) == 9:
        done[0] = True
    if not done[1] and len(min(y,key=len)) == 9:
        done[1] = True
    if not done[2] and len(min(z,key=len)) == 9:
        done[2] = True

    if all(done):
        for i in puzzles:
            print(''.join(map(str,i)))
        break
