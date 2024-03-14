'''
Unique Paths in a Grid with Obstacles and Boosters

You're given a 2D grid representing a field, where you can move either right or down at each step.
The grid has the following characteristics:

0 represents a free cell where you can move.
1 represents an obstacle that you cannot move onto.
2 represents a booster. Landing on this cell doubles your speed, allowing you to move two steps at a time either right or down in subsequent moves.
If you land on another booster while moving at double speed, it has no additional effect (you can't move four steps at a time, for example).
You start in the top-left corner at (0, 0) and
want to reach the bottom-right corner (m-1, n-1).
You can assume that the start and end cells are always free, and there's at least one path to the end.

Input:

A 2D list grid representing the field, where grid[i][j] is the cell's value.

Output:

The total number of unique paths from start to end. Since the answer can be large, return it modulo 10^9 + 7.
Constraints:

1 <= m, n <= 100
The grid will contain only 0, 1, and 2.
Example:

plaintext

Input: grid = [
  [0, 0, 0],
  [0, 1, 0],
  [2, 0, 0]
]

Output: 3

Explanation:
There are two paths from the top-left corner to the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Right -> Down -> Down -> Right (After moving down into a cell with a booster, the next move is a double step down.)
Solution Approach:
This problem adds an interesting layer to the classic "unique paths" problem by introducing obstacles and speed boosters,
making it necessary to track the state of the traveler's speed in addition to their position.

A dynamic programming solution can be extended to account for these conditions. For each cell (i, j),
maintain counts of the number of ways to reach that cell with and without a speed boost. When you encounter a booster, update the counts accordingly, considering the ability to move two steps in subsequent moves.

Consider breaking down the problem into subproblems, where each subproblem solves for the number of unique paths to reach a cell (i, j) under different conditions (normal speed and boosted speed).

'''

MOD = 10**9 + 7

def unique_paths_with_obstacles_and_boosters(grid):
    m, n = len(grid), len(grid[0])
    # DP table dimensions: m x n x 2, with an additional state for booster usage
    dp = [[[0, 0] for _ in range(n)] for _ in range(m)]
    dp[0][0][0] = 1  # Starting position, without using booster

    for i in range(m):
        for j in range(n):
            for boost in range(2):  # Iterate through booster states
                # Regular move right or down
                for di, dj in [(0, 1), (1, 0)]:
                    ni, nj = i + di, j + dj
                    if ni < m and nj < n and grid[ni][nj] != 1:
                        dp[ni][nj][boost] += dp[i][j][boost]
                        dp[ni][nj][boost] %= MOD

                # If on a booster and not used yet
                if grid[i][j] == 2 and boost == 0:
                    for di, dj in [(0, 2), (2, 0)]:
                        ni, nj = i + di, j + dj
                        if ni < m and nj < n and grid[ni][nj] != 1:
                            # Check for obstacle in the skipped cell for diagonal moves
                            if (di == 0 or grid[i+1][j] != 1) and (dj == 0 or grid[i][j+1] != 1):
                                dp[ni][nj][1] += dp[i][j][0]  # Use booster
                                dp[ni][nj][1] %= MOD

    # Return the sum of ways to reach the end, with and without using the booster
    return (dp[m-1][n-1][0] + dp[m-1][n-1][1]) % MOD

# Example input
grid = [
  [0, 0, 0],
  [0, 1, 0],
  [2, 0, 0]
]

grid2 = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 2, 0, 1, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 2, 0, 0, 0, 0],
]

# Calculate and print the total number of unique paths

total_paths = unique_paths_with_obstacles_and_boosters(grid)
total_paths2 = unique_paths_with_obstacles_and_boosters(grid2)
print(f"Total unique paths: {total_paths}")
print(f"Total unique paths: {total_paths2}")

