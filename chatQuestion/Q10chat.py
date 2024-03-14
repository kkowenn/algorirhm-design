'''
[10 Marks] Treasure Hunt in the Mystic Ruins

In an ancient ruin, a treasure hunter aims to collect as many relics as possible.
The ruin is represented as a grid, where each cell may contain a certain number of relics or may be a trap.
The hunter starts from the top-left corner of the grid and can only move right or down.
The objective is to find the path that allows the hunter to collect the maximum number of relics without hitting a trap.

Given the grid, where each cell contains either the number of relics or a symbol representing a trap (X),
develop a Python program to compute the maximum number of relics that can be collected by any path from the top-left corner to the bottom-right corner.

INPUT:

The first line contains an integer N (1 ≤ N ≤ 20), the size of the square grid (NxN).
Each of the next N lines contains N space-separated values, which are either non-negative integers representing the number of relics in that cell or the letter 'X' representing a trap.
OUTPUT:

A single integer representing the maximum number of relics that can be collected.
If there is no path to reach the bottom-right corner without hitting a trap, output Impossible.
EXAMPLE

INPUT:

4
0 2 X 1
1 X 3 2
X 0 0 4
3 1 2 0
OUTPUT:

9
Elaboration:
One possible path that collects the maximum number of relics is as follows: start at (0,0) with 0 relics, 
move right to (0,1) with 2 relics,
move down to (1,1) collecting no relics due to the trap,
move down to (2,1) with 2 relics, 
move right to (2,2) with 2 relics,
move right to (2,3) with 6 relics,
and finally move down to (3,3) ending with 9 relics.
Other paths may lead to traps or collect fewer relics.
'''

def max_relics(grid, N):
    # Initialize a 2D list to store the maximum relics collected up to each cell
    dp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # If it's the first cell and not a trap, initialize it with its own value
            if i == 0 and j == 0 and grid[i][j] != 'X':
                dp[i][j] = int(grid[i][j])
                continue
            # If the current cell is a trap, continue to the next cell
            if grid[i][j] == 'X':
                dp[i][j] = -1
                continue
            # Take the maximum of the top or left cell values if they are not traps, and add current cell relics
            if i > 0 and dp[i-1][j] != -1:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + int(grid[i][j]))
            if j > 0 and dp[i][j-1] != -1:
                dp[i][j] = max(dp[i][j], dp[i][j-1] + int(grid[i][j]))

    # If the bottom-right cell is a trap or unreachable, return Impossible
    if dp[N-1][N-1] == -1:
        return "Impossible"

    return dp[N-1][N-1]

# Read input
N = int(input())
grid = [input().split() for _ in range(N)]

# Call the function and print the result
print(max_relics(grid, N))
