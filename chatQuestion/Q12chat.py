'''
10 Marks] Chrono-Conservationist's Dilemma

In a distant future, a Chrono-Conservationist works to restore extinct species by collecting DNA samples from various time periods.
The time machine used for this mission can jump to different eras on a temporal grid, where each cell represents a specific time period in history,
identifiable by coordinates (Era, Year). The grid contains certain anomalies that must be avoided.

Given a temporal grid with N eras, each having M years, and a list of anomalies, the Chrono-Conservationist needs to plot a course from the origin of time (0, 0) to the present (N-1, M-1) to collect as much diverse DNA as possible.
Each cell in the temporal grid contains an integer representing the diversity value of DNA that can be collected. Anomalies are represented by a negative value and must not be crossed.

The time machine can move only to the right (to the future within the same era) or down (to a different era in the same year), representing the constraints of time travel technology.
The goal is to find the path with the maximum sum of DNA diversity values.

INPUT:

The first line contains two integers N and M (1 ≤ N, M ≤ 100), the number of eras and years in the temporal grid, respectively.
The next N lines each contain M integers, representing the DNA diversity values or anomalies in each cell. A positive integer v represents a DNA diversity value, while -1 represents an anomaly.
OUTPUT:

A single integer representing the maximum sum of DNA diversity values that can be collected along a path from (0, 0) to (N-1, M-1), avoiding anomalies. If no such path exists, output Extinction.
EXAMPLE

INPUT:

5 5
2 3 -1 1 4
1 -1 2 3 2
4 1 1 -1 3
3 2 -1 4 2
-1 3 2 1 5
OUTPUT:

20
Elaboration:
The optimal path might be: Start at (0,0) with value 2, move right to (0,1) with value 3, move down to (1,1) avoiding the anomaly, and continue moving down and to the right, avoiding negative values, collecting a maximum sum of diversity values.

This problem can be approached using dynamic programming to navigate the constraints of time travel and biological data collection, with a compelling twist on conservation biology.
'''

def max_dna_diversity(grid):
    N, M = len(grid), len(grid[0])
    dp = [[0] * M for _ in range(N)]

    # Initialize the dp table, taking care not to cross anomalies
    for era in range(N):
        for year in range(M):
            if grid[era][year] == -1:
                dp[era][year] = float('-inf')
            else:
                left = dp[era][year - 1] if year > 0 else 0
                up = dp[era - 1][year] if era > 0 else 0
                dp[era][year] = max(left, up) + grid[era][year]

    # If the present cell has a value of float('-inf'), it means there's no valid path.
    if dp[N-1][M-1] == float('-inf'):
        return "Extinction"

    return dp[N-1][M-1]

# Example input processing
N, M = map(int, input().split())
temporal_grid = [list(map(int, input().split())) for _ in range(N)]

print(max_dna_diversity(temporal_grid))
