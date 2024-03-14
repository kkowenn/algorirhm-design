M, N = map(int, input().split())
matrix = []
box = (0, 0)
target = (0, 0)
player = (0, 0)
for i in range(N):
    row = input().split()
    matrix.append(row)
    for j in range(M):
        if row[j] == 'B':
            box = (i, j)
        elif row[j] == 'T':
            target = (i, j)
        elif row[j] == 'S':
            player = (i, j)

class State:
    def __init__(self, player, box, moves=0):
        self.player = player
        self.box = box
        self.moves = moves  # Track moves for this state

def goal(box, target):
    return box == target

def valid(x, y, matrix):
    return 0 <= x < N and 0 <= y < M and matrix[x][y] != '#'

# Assuming the initial setup is done as before
def bfs(matrix, start, box, target):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
    queue = [(start, box, 0)]  # (player position, box position, moves)
    visited = set([(start, box)])

    while queue:
        current_state = queue[0]
        queue = queue[1:]  # Remove the first element
        player_pos, box_pos, moves = current_state

        if box_pos == target:
            return moves

        for d in directions:
            new_player_pos = (player_pos[0] + d[0], player_pos[1] + d[1])
            # Move player to new position if valid and not blocked
            if 0 <= new_player_pos[0] < N and 0 <= new_player_pos[1] < M and matrix[new_player_pos[0]][new_player_pos[1]] != '#' and new_player_pos != box_pos:
                if (new_player_pos, box_pos) not in visited:
                    visited.add((new_player_pos, box_pos))
                    queue.append((new_player_pos, box_pos, moves))

            # Push the box if next to it and the move is valid
            if new_player_pos == box_pos:
                new_box_pos = (box_pos[0] + d[0], box_pos[1] + d[1])
                if 0 <= new_box_pos[0] < N and 0 <= new_box_pos[1] < M and matrix[new_box_pos[0]][new_box_pos[1]] != '#' and (new_player_pos, new_box_pos) not in visited:
                    visited.add((new_player_pos, new_box_pos))
                    queue.append((box_pos, new_box_pos, moves + 1))

    return -1


result = bfs(matrix, player, box, target)
print(result if result != -1 else "-1")
