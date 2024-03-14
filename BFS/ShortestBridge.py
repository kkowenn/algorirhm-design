'''
934. Shortest Bridge
Medium

Topics
Companies
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.



Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1


Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
'''

# Time:  O(n^2)
# Space: O(n^2)

import collections


class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def get_islands(A):
            islands = []
            done = set()
            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    if val == 0 or (r, c) in done:
                        continue
                    s = [(r, c)]
                    lookup = set(s)
                    while s:
                        node = s.pop()
                        for d in directions:
                            nei = node[0]+d[0], node[1]+d[1]
                            if not (0 <= nei[0] < len(A) and 0 <= nei[1] < len(A[0])) or \
                               nei in lookup or A[nei[0]][nei[1]] == 0:
                                continue
                            s.append(nei)
                            lookup.add(nei)
                    done |= lookup
                    islands.append(lookup)
                    if len(islands) == 2:
                        break
            return islands

        lookup, target = get_islands(A)
        q = collections.deque([(node, 0) for node in lookup])
        while q:
            node, dis = q.popleft()
            if node in target:
                return dis-1
            for d in directions:
                nei = node[0]+d[0], node[1]+d[1]
                if not (0 <= nei[0] < len(A) and 0 <= nei[1] < len(A[0])) or \
                   nei in lookup:
                    continue
                q.append((nei, dis+1))
                lookup.add(nei)


class Solution2(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def get_islands(A):
            islands = []
            done = set()
            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    if val == 0 or (r, c) in done:
                        continue
                    s = [(r, c)]
                    lookup = set(s)
                    while s:
                        node = s.pop()
                        for d in directions:
                            nei = node[0] + d[0], node[1] + d[1]
                            if not (0 <= nei[0] < len(A) and 0 <= nei[1] < len(A[0])) or \
                               nei in lookup or A[nei[0]][nei[1]] == 0:
                                continue
                            s.append(nei)
                            lookup.add(nei)
                    done |= lookup
                    islands.append(lookup)
                    if len(islands) == 2:
                        break
            return islands

        def bfs(start, target):
            q = [(start, 0)]
            visited = {start}
            while q:
                node, dis = q.pop(0)
                if node in target:
                    return dis - 1
                for d in directions:
                    nei = node[0] + d[0], node[1] + d[1]
                    if not (0 <= nei[0] < len(A) and 0 <= nei[1] < len(A[0])) or \
                       nei in visited:
                        continue
                    q.append((nei, dis + 1))
                    visited.add(nei)
            return -1

        islands = get_islands(A)
        return bfs(islands[0].pop(), islands[1])


# Test case
solution = Solution()
solution2 = Solution2()
grid1 = [[0,1],[1,0]]
grid2 = [[0,1,0],[0,0,0],[0,0,1]]
grid3 = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]

print(solution.shortestBridge(grid1))
print(solution2.shortestBridge(grid1))
print(solution.shortestBridge(grid2))
print(solution2.shortestBridge(grid2))
print(solution.shortestBridge(grid3))
print(solution2.shortestBridge(grid3))
print("So the solution2 is wrong grid3 supposed to be 1")
