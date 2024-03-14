# 0 = grass
# 1 = fire
# 2 = a wall that you and fire cannot pass through

class State:
    def __init__(self, x, y, time, is_fire):
        self.x = x
        self.y = y
        self.time = time
        self.is_fire = is_fire  # True for fire, False for people

def goal(x, y, m, n):
    return x == m - 1 and y == n - 1

def valid(x, y, m, n, A, visited, is_fire):
    return 0 <= x < m and 0 <= y < n and A[x][y] == 0 and visited[x][y][is_fire] == -1

def bfs(A):
    m, n = len(A), len(A[0])
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Initializing visited with [fire_time, ppl_time]
    # not visited all , make the matrix be -1
    visited = [[[-1, -1] for _ in range(n)] for _ in range(m)]
    Q = []
    # Adding fire states
    for x in range(m):
        for y in range(n):
            if A[x][y] == 1:
                Q.append(State(x, y, 0, True))
                visited[x][y][True] = 0
    Q.append(State(0, 0, 0, False))
    # ไม่มีไฟ set 0 แก้ไอเวรนี้ not visited all , make the matrix be -1 ให้ 0 คนเดินได้
    visited[0][0][False] = 0

    while Q:
        state = Q[0]
        del Q[0]
        if goal(state.x, state.y, m, n):
            continue  # Goal check not needed for BFS but could be useful for termination
        for dx, dy in dirs:
            nx, ny = state.x + dx, state.y + dy
            if valid(nx, ny, m, n, A, visited, state.is_fire):
                Q.append(State(nx, ny, state.time + 1, state.is_fire))
                visited[nx][ny][state.is_fire] = state.time + 1

    return visited

def maximumMinutes(A):
    # Get the dimensions of the grid
    m, n = len(A), len(A[0])

    # Compute the time it takes for fire and people to reach each cell in the grid
    visited = bfs(A)

    # Extract the time it takes for people and fire to reach the bottom-right cell
    ppl_time = visited[-1][-1][False]
    fire_time = visited[-1][-1][True]

    # Check various conditions to determine the result
    # If people cannot reach the destination, return -1
    if ppl_time == -1:
        return -1

    # If fire cannot reach the destination, return a large value (10^9)
    if fire_time == -1:
        return 10 ** 9

    # If fire reaches the destination before people, return -1 (caught by fire)
    if fire_time < ppl_time:
        return -1

    # Calculate the time difference between fire and people reaching the destination
    diff = fire_time - ppl_time

    # Extract the times for adjacent cells to the destination, considering both fire and people
    ppl_1, ppl_2 = visited[-1][-2][False], visited[-2][-1][False]
    fire_1, fire_2 = visited[-1][-2][True], visited[-2][-1][True]

    # Check if there are adjacent cells that fire can reach before people
    # Adjust the result accordingly
    if ppl_1 > -1 and ppl_2 > -1 and (fire_1 - ppl_1 > diff or fire_2 - ppl_2 > diff):
        return diff  # Return diff if conditions are met
    return diff - 1  # Otherwise, return diff - 1


H, T = map(int, input().split())
m = []
for t in range(T):
    x = list(map(int, input().split()))
    m.append(x)

result = maximumMinutes(m)
print(result)
