'''
[10 Marks] City Delivery Drone Routing

A logistics company is experimenting with drones for delivering small packages across a city.
The city is represented as a grid where each cell can be a building (unpassable), an open space (passable), or a no-fly zone (unpassable).
he company aims to find the shortest path for a drone to deliver a package from the warehouse to a customer's location, avoiding no-fly zones and buildings.

Given the city's grid map, the warehouse location, and the customer's location, develop a Python program to compute the shortest delivery path for the drone. If it's impossible to reach the customer due to obstructions, the program should indicate so.

INPUT:

The first line contains two integers H and W (1 ≤ H, W ≤ 100), the height and width of the grid.
Each of the next H lines contains W characters, representing the city grid. Each character can be:
. (dot) for open space,
# (hash) for building/no-fly zone,
W for the warehouse (starting point),
C for the customer's location (destination).
It's guaranteed that there is exactly one W and one C in the grid.
OUTPUT:

The minimum number of steps (moving up, down, left, or right) required for the drone to reach the customer from the warehouse, or Impossible if the customer cannot be reached.
EXAMPLE

INPUT:

5 5
.....
.#.#.
.W.#C
.###.
.....
OUTPUT:

9
Elaboration:
The drone starts at W, moves right 1 step, up 2 steps, right 2 steps, down 2 steps, and finally right 2 steps to reach C, totaling 9 steps. Direct paths are blocked by buildings or no-fly zones.

This problem is a classic example of grid-based pathfinding, where algorithms like Breadth-First Search (BFS) are perfectly suited due to their ability to find the shortest path in unweighted graphs (or grids, in this case).
'''

from simplePriorityQueue import Simple_Priority_Queue


def bfs(grid, start, end):
    H, W = len(grid), len(grid[0])
    visited = [[False]*W for _ in range(H)]
    queue = Simple_Priority_Queue()
    queue.enqueue((start, 0))  # (position, steps)
    while queue:
        (x, y), steps = queue.dequeue()  # Correct dequeue usage
        if (x, y) == end:
            return steps
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] in ('.', 'C'):
                visited[nx][ny] = True
                queue.enqueue(((nx, ny), steps + 1))
    return "Impossible"

H, W = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]

start = end = None
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'W':
            start = (i, j)
        elif grid[i][j] == 'C':
            end = (i, j)

print(bfs(grid, start, end))
