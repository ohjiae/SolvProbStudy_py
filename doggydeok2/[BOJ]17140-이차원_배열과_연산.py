import heapq


def simulate(_r, _c, _k):
    row_cnt_arr = [[0] * 101 for _ in range(100)]
    col_cnt_arr = [[0] * 101 for _ in range(100)]
    arr = [[0] * 100 for _ in range(100)]
    max_r = max_c = 3
    for i in range(3):
        arr[i][0], arr[i][1], arr[i][2] = map(int, input().split())
        for j in range(3):
            row_cnt_arr[i][arr[i][j]] += 1
            col_cnt_arr[j][arr[i][j]] += 1

    for t in range(100):
        if arr[_r][_c] == _k:
            return t
        heap = []
        if max_r >= max_c:
            # R calculation
            for i in range(100):
                for idx, num in enumerate(row_cnt_arr[i]):
                    if idx == 0 or num == 0:
                        continue
                    heapq.heappush(heap, (num, idx))
                # clear and fill
                this_c = 0
                for j in range(0, 100, 2):
                    row_cnt_arr[i][arr[i][j]] -= 1
                    row_cnt_arr[i][arr[i][j + 1]] -= 1
                    col_cnt_arr[j][arr[i][j]] -= 1
                    col_cnt_arr[j + 1][arr[i][j + 1]] -= 1
                    if heap:
                        cnt, val = heapq.heappop(heap)
                        row_cnt_arr[i][val] += 1
                        row_cnt_arr[i][cnt] += 1
                        col_cnt_arr[j][val] += 1
                        col_cnt_arr[j + 1][cnt] += 1

                        arr[i][j] = val
                        arr[i][j + 1] = cnt
                        this_c += 2
                    else:
                        arr[i][j] = 0
                        arr[i][j + 1] = 0
                max_c = max(max_c, this_c)
        else:
            # C calculation
            for i in range(100):
                for idx, num in enumerate(col_cnt_arr[i]):
                    if idx == 0 or num == 0:
                        continue
                    heapq.heappush(heap, (num, idx))
                # clear and fill
                this_r = 0
                for j in range(0, 100, 2):
                    row_cnt_arr[j][arr[j][i]] -= 1
                    row_cnt_arr[j + 1][arr[j + 1][i]] -= 1
                    col_cnt_arr[i][arr[j][i]] -= 1
                    col_cnt_arr[i][arr[j + 1][i]] -= 1
                    if heap:
                        cnt, val = heapq.heappop(heap)
                        row_cnt_arr[j][val] += 1
                        row_cnt_arr[j + 1][cnt] += 1
                        col_cnt_arr[i][val] += 1
                        col_cnt_arr[i][cnt] += 1

                        arr[j][i] = val
                        arr[j + 1][i] = cnt
                        this_r += 2
                    else:
                        arr[j][i] = 0
                        arr[j + 1][i] = 0
                max_r = max(max_r, this_r)

    return 100 if arr[_r][_c] == _k else -1


r, c, k = map(int, input().split())
r, c = r - 1, c - 1
print(simulate(r, c, k))
