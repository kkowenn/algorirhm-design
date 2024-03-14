from itertools import product
from typing import List

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        #constants
        m, n = len(grid), len(grid[0]) #dimensions
        neighbors = ((-1,0), (1,0), (0,-1), (0,1))

        #initial values
        for i, j in product(range(m), range(n)):
            if   grid[i][j] == "B": box    = i, j
            elif grid[i][j] == "S": player = i, j
            elif grid[i][j] == "T": target = i, j

        #helper functions
        not_wall = lambda i, j: 0 <= i < m and 0 <= j < n and grid[i][j] !="#" #true if not wall

        def connected(s, d):
            """bfs to check if s and d are connected"""
            queue = [s]
            seen = set(queue)
            for i, j in queue: #okay to change size
                for di, dj in neighbors:
                    ii, jj = i + di, j + dj
                    if not_wall(ii, jj) and (ii, jj) != box and (ii, jj) not in seen:
                        queue.append((ii, jj))
                        seen.add((ii, jj))
                if d in seen: return True
            return False

        #logic -- nested bfs
        final = set((target, (target[0]+di, target[1]+dj)) for di, dj in neighbors)

        moves = 0
        queue = [(box, player)] #initial position
        seen = set(queue)
        while queue: #bfs by level
            temp = []
            for box, player in queue:
                i, j = box
                for di, dj in neighbors:
                    if not_wall(i+di, j+dj) and ((i+di, j+dj), (i, j)) not in seen and not_wall(i-di, j-dj) and connected(player, (i-di, j-dj)):
                        temp.append(((i+di, j+dj), (i, j)))
                        seen.add(((i+di, j+dj), (i, j)))
            queue = temp
            moves += 1
            if seen & final: return moves #final configuration => arrive at target
        return -1

M, N = map(int, input().split())
matrix = []
for _ in range(N):
    row = input().split()
    matrix.append(row)

solution = Solution()
result = solution.minPushBox(matrix)

print(result)
