from collections import deque
from sys import stdin
input = stdin.readline
puzzles = [list(map(int,list(input().rstrip()))) for _ in range(9)]
zeros = deque()
xnums, ynums, znums = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
# 0 위치 체크 (#가진거 체크)
for nx in range(9):
    for ny in range(9):
        z = (nx // 3, ny // 3)
        if not z[0]:
            nz = z[1]
        elif z[0] == 1:
            nz = z[1] + 3
        else:
            nz = z[1] + 6

        num = puzzles[nx][ny]
        if num == 0:
            zeros.append((nx,ny,nz))
        else :
            xnums[nx].add(num)
            ynums[ny].add(num)
            znums[nz].add(num)

while zeros:
    x,y,z = zeros.popleft()
    now = puzzles[x][y]
    nlist = (set(range(1,10)) if not now else now)
    tmp = set()
    for n in nlist:
        if n not in xnums[x] and n not in ynums[y] and n not in znums[z]:
            tmp.add(n)
    if len(tmp) == 1:
        tara = tmp.pop()
        xnums[x].add(tara)
        ynums[y].add(tara)
        znums[z].add(tara)
        puzzles[x][y] = tara
    else:
        puzzles[x][y] = tmp
        zeros.append((x,y,z))

for i in puzzles:
    print(''.join(map(str,i)))


# x,y,z중 가장 긴 원소를 가진 리스트 찾기
# def find_long():
#     xyz = [('x',max(x,key=len)),('y',max(y,key=len)),('z',max(z,key=len))]
#     xyz.sort(key= lambda x: len(x[1]),reverse=True)
#     return xyz[0][0]
