from collections import deque
from typing import List

def maximumMinutes(A: List[List[int]]) -> int:
    m, n = len(A), len(A[0])
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    ppl_time = [[-1] * n for _ in range(m)]
    fire_time = [[-1] * n for _ in range(m)]

    # BFS for people's arrival for each cell.
    ppl_front = deque([(0, 0, 0)])
    while ppl_front:
        cx, cy, days = ppl_front.popleft()
        ppl_time[cx][cy] = days
        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < m and 0 <= ny < n and A[nx][ny] == 0 and ppl_time[nx][ny] == -1:
                ppl_front.append((nx, ny, days + 1))

    # BFS for fire's arrival for each cell.
    fire_front = deque([(x, y, 0) for x in range(m) for y in range(n) if A[x][y] == 1])
    while fire_front:
        cx, cy, days = fire_front.popleft()
        fire_time[cx][cy] = days
        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < m and 0 <= ny < n and A[nx][ny] == 0 and fire_time[nx][ny] == -1:
                fire_front.append((nx, ny, days + 1))

    # Check the arrival days for the bottom-right cell.
    ppl_arrival = ppl_time[-1][-1]
    fire_arrival = fire_time[-1][-1]

    # Some edge cases.
    if ppl_arrival == -1:
        return -1
    if fire_arrival == -1:
        return 10 ** 9
    if fire_arrival < ppl_arrival:
        return -1

    # Whether we are 'followed' by fire on both two paths toward bot-right cell.
    diff = fire_arrival - ppl_arrival
    ppl_1, ppl_2 = ppl_time[-1][-2], ppl_time[-2][-1]

    fire_1, fire_2 = fire_time[-1][-2], fire_time[-2][-1]
    if ppl_1 > -1 and ppl_2 > -1 and (fire_1 - ppl_1 > diff or fire_2 - ppl_2 > diff):
        return diff
    return diff - 1

H, T = map(int, input().split())
m = []
for t in range(T):
    x = list(map(int, input().split()))
    m.append(x)

result = maximumMinutes(m)
print(result)
