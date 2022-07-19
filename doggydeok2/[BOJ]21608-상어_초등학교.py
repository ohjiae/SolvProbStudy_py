def check_adj_empty(_x):
    _r, _c = _x
    able_adj = []
    for k in range(4):
        nr, nc = _r + dij[k], _c + dij[k + 1]
        if 0 <= nr < N and 0 <= nc < N and not classroom[nr][nc]:
            able_adj.append([nr, nc])
    return able_adj


def get_seat_for_oneself():
    ans, ans_adj_empty_cnt = [], -1
    for x in range(N):
        for y in range(N):
            if classroom[x][y] == 0:
                adj_empty = check_adj_empty([x, y])
                if len(adj_empty) > ans_adj_empty_cnt:
                    ans = [x, y]
                    ans_adj_empty_cnt = len(adj_empty)
                    if ans_adj_empty_cnt == 4:
                        return ans
    return ans


dij = [0, -1, 0, 1, 0]
N = int(input())
classroom = [[0] * N for _ in range(N)]
friends = [[] for _ in range(N ** 2 + 1)]
students = []
for _ in range(N ** 2):
    n, a, b, c, d = map(int, input().split())
    friends[n] = [a, b, c, d]
    students.append(n)

seated = [False] * (N ** 2 + 1)
for student in students:
    targets = []

    for friend in friends[student]:
        if seated[friend]:
            targets.extend(check_adj_empty(seated[friend]))

    if targets:
        targets.sort()
        cnt_dict = {}
        for target in targets:
            rc = target[0] * 1000 + target[1]
            if cnt_dict.get(rc) is None:
                cnt_dict[rc] = 1
            else:
                cnt_dict[rc] += 1

        picked = picked_cnt = empty_cnt = -1
        for rc, cnt in sorted(cnt_dict.items(), key=lambda f: (-f[1], f[0])):
            if picked_cnt <= cnt:
                empty_adj_seat = len(check_adj_empty([rc // 1000, rc % 1000]))
                if empty_cnt < empty_adj_seat:
                    empty_cnt = empty_adj_seat
                    picked_cnt = cnt
                    picked = rc
            else:
                break

        classroom[picked // 1000][picked % 1000] = student
        seated[student] = [picked // 1000, picked % 1000]
    else:
        tr, tc = get_seat_for_oneself()
        classroom[tr][tc] = student
        seated[student] = [tr, tc]

total_satisfaction = 0
for i in range(N):
    for j in range(N):
        satisfaction = 1
        student = classroom[i][j]
        for friend in friends[student]:
            fi, fj = seated[friend]
            if abs(fi - i) + abs(fj - j) == 1:
                satisfaction *= 10
        total_satisfaction += satisfaction // 10
print(total_satisfaction)
