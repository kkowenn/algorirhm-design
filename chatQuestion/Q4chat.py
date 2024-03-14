'''
[10 Marks] Smart City Lighting

In an effort to reduce energy consumption, a smart city plans to optimize its street lighting.
The city is laid out in a grid, with lights at every intersection.
Due to advancements in technology, each light can be programmed to illuminate multiple intersections in its row and column.
However, activating a light incurs an energy cost, and the goal is to minimize the total energy cost while ensuring every intersection is illuminated.

Given a grid representing the city layout, with each cell indicating the energy cost of activating the light at that intersection,
develop a Python program that calculates the minimum total energy cost to illuminate all intersections.

INPUT:

The first line contains two integers H and W (1 ≤ H, W ≤ 100), the height and width of the grid.
The next H lines each contain W integers, representing the energy cost of activating the light at each intersection.
OUTPUT:

A single integer representing the minimum total energy cost to illuminate all intersections.
EXAMPLE

INPUT:
3 4
1 2 3 4
2 1 2 3
3 4 1 2

OUTPUT:

4
Elaboration:
The optimal strategy involves activating the lights at intersections (2,2) and (3,3), with energy costs 1 and 1 respectively,
covering the entire grid at the minimum total cost of 2. This ensures every intersection is illuminated by at least one light,
achieving the goal with minimal expenditure.

This problem challenges solvers to think creatively about covering a grid efficiently, akin to a modified version of the set cover problem,
but with the unique twist of intersecting rows and columns from activated points.
It nudges towards considering dynamic programming or greedy algorithms to find a cost-effective set of intersections for activation.
'''


def illuminate(grid):
    H, W = len(grid), len(grid[0])
    illuminated = [[False] * W for _ in range(H)]
    total_cost = 0

    # Function to count dark intersections in a row or column
    def count_dark(row=None, col=None):
        count = 0
        if row is not None:
            for c in range(W):
                if not illuminated[row][c]:
                    count += 1
        elif col is not None:
            for r in range(H):
                if not illuminated[r][col]:
                    count += 1
        return count

    # Keep activating lights until all intersections are illuminated
    while any(not all(row) for row in illuminated):
        best_cost_per_dark = float('inf')
        best_choice = None
        for r in range(H):
            for c in range(W):
                if not illuminated[r][c]:
                    dark_in_row = count_dark(row=r)
                    dark_in_col = count_dark(col=c)
                    total_dark = dark_in_row + dark_in_col - 1  # Intersection counted twice
                    cost_per_dark = grid[r][c] / total_dark if total_dark else float('inf')

                    if cost_per_dark < best_cost_per_dark:
                        best_cost_per_dark = cost_per_dark
                        best_choice = (r, c)

        # Illuminate chosen intersection and update
        if best_choice:
            r, c = best_choice
            for i in range(W):
                illuminated[r][i] = True
            for i in range(H):
                illuminated[i][c] = True
            total_cost += grid[r][c]

    return total_cost

# Example input processing
H, W = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

print(illuminate(grid))
