class Solution:
    def countOfPairs(self, n: int, x: int, y: int):
        # Initialize a list to store the count of pairs for each distance
        res = [0] * n

        # Create a list of lists for the houses and streets
        adjacency_list = [[] for _ in range(n + 1)]

        # Add edges for streets connecting houses
        for i in range(1, n):
            adjacency_list[i].append(i + 1)
            adjacency_list[i + 1].append(i)

        # Add the additional street connecting house x and house y
        adjacency_list[x].append(y)
        adjacency_list[y].append(x)

        # Define a BFS function to find the minimum distance from a house
        def bfs(i):
            q = []
            visit = set()
            q.append((i, 0))
            visit.add(i)

            while q:
                state = q[0]
                del q[0]
                i, dist = state

                if dist > 0:
                    res[dist - 1] += 1

                for nei in adjacency_list[i]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append((nei, dist + 1))

        # Iterate through each house and perform BFS
        for i in range(1, n + 1):
            bfs(i)

        return res

# Input values
n, x, y = map(int, input().split())

# Create an instance of the Solution class
solution_instance = Solution()

# Call the countOfPairs method
result = solution_instance.countOfPairs(n, x, y)

# Print the result
print(result)
