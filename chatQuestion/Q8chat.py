'''
[10 Marks] Optimal Water Distribution in a Drought-Stricken Area

A drought-stricken region is implementing a water distribution plan to ensure all its villages receive necessary water supplies.
The region is divided into several villages, and a network of pipelines connects these villages.
Each pipeline can carry a fixed amount of water per day from one village to another,
but due to varying distances and capacities, the cost of pumping water through each pipeline varies.

Given a list of villages, the pipelines connecting them along with their daily water carrying capacity and the cost per unit of water,
and the daily water requirement for each village, develop a Python program that calculates the minimum total cost to satisfy the daily water requirements of all villages.

INPUT:

The first line contains two integers V and P (1 ≤ V ≤ 1000, 1 ≤ P ≤ 5000), the number of villages and pipelines, respectively.
The next line contains V integers, representing the daily water requirement (in cubic meters) for each village.
Each of the next P lines contains four integers A, B, C, and D, representing a pipeline from village A to village B with a capacity of C cubic meters per day and a cost of D dollars per cubic meter.
OUTPUT:

A single integer representing the minimum total cost to distribute water so that each village's daily requirement is met. If it's impossible to meet all villages' requirements with the given pipelines, print Impossible.
EXAMPLE

INPUT:

4 5
10 20 15 5
1 2 20 2
1 3 15 4
2 4 15 3
3 4 10 2
1 4 5 6
OUTPUT:


130
Elaboration:
To meet the daily requirements, water is distributed through the pipelines as follows:

10 cubic meters from Village 1 to Village 2 at a cost of 2 dollars per cubic meter.
15 cubic meters from Village 1 to Village 3 at a cost of 4 dollars per cubic meter.
5 cubic meters from Village 1 to Village 4 directly at a cost of 6 dollars per cubic meter (or choose the path through Villages 2 and 3 to Village 4 for potentially lower cost).
The remaining needs of Villages 2 and 4 are met by the capacities of pipelines from Village 2 to Village 4 and Village 3 to Village 4.
The goal is to use the pipelines efficiently to minimize the total cost while ensuring that the water requirements of all villages are satisfied.
'''

from collections import defaultdict
import heapq

def min_cost_flow(villages, pipelines):
    graph = defaultdict(list)
    for a, b, capacity, cost in pipelines:
        # Directed graph: (destination, capacity, cost)
        graph[a].append((b, capacity, cost))
        graph[b].append((a, 0, -cost))  # Reverse edge for flow cancellation

    # Bellman-Ford or Dijkstra with potential can be used to find min cost paths
    # This example is a simplified version and needs adjustments for a full solution.

    def find_min_cost_path(source, sink, demand):
        # Placeholder for path finding and flow adjustment
        pass

    total_cost = 0
    for village, requirement in enumerate(villages, 1):
        if requirement > 0:
            cost = find_min_cost_path(1, village, requirement)
            if cost is None:
                return "Impossible"
            total_cost += cost

    return total_cost

V, P = map(int, input().split())
requirements = list(map(int, input().split()))
pipelines = [list(map(int, input().split())) for _ in range(P)]

print(min_cost_flow(requirements, pipelines))

