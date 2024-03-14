'''
Problem: Optimal Resource Merging for Projects
In a development environment, you are managing a set of projects that require varying amounts of resources to complete.
Each project is initially treated as an individual resource block. You can merge any two projects at a time to form a larger combined project,
but doing so incurs a cost proportional to the sum of the sizes of the two projects being merged.

Your goal is to merge all these individual projects into a single project block in such a way that minimizes the total cost of merging.

Input:

A list of integers projects, where each integer represents the size of a project.

Output:

The minimum possible total cost to merge all the projects into one.
Example:

Input: projects = [10, 20, 30, 40, 50]

Output: 330

Explanation:
1. Merge projects of size 10 and 20 (cost = 30), remaining projects = [30, 30, 40, 50]
2. Merge projects of size 30 and 30 (cost = 60), remaining projects = [60, 40, 50]
3. Merge projects of size 40 and 50 (cost = 90), remaining projects = [60, 90]
4. Merge the last two projects (cost = 150), total cost = 30 + 60 + 90 + 150 = 330
Solution Approach:

This problem can also be approached using a greedy algorithm, specifically utilizing a priority queue or min heap to always merge the two smallest projects first.
This approach is based on the observation that merging smaller projects earlier reduces the overall cost, similar to the Huffman coding algorithm.

'''
import heapq

def minCostToMergeProjects(projects):
    # Initialize total cost to 0
    total_cost = 0

    # Create a min heap from the projects list
    heapq.heapify(projects)

    # Continue merging until we have one project left
    while len(projects) > 1:
        # Pop the two smallest projects
        smallest = heapq.heappop(projects)
        second_smallest = heapq.heappop(projects)

        # The cost of merging these two projects
        cost = smallest + second_smallest

        # Add the cost to the total cost
        total_cost += cost

        # Push the merged project back into the min heap
        heapq.heappush(projects, cost)

    return total_cost

# Example usage
projects = [10, 20, 30, 40, 50]
print(minCostToMergeProjects(projects))
