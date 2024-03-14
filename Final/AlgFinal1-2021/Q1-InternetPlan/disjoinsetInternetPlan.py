'''
Sinking Ship

Lupin is training himself with simulation of a crisis scenario. This time, the crisis he
simulated is sinking cruise ship.

A gigantic cruise ship is hit an underwater iceburg and is sinking. Water is flooding the bilge
and passengers are evacuating to life boats. Lupin the thief, however, finds this to be the time
that he can take valuable things of others without being caught. He has the map of all the
valuable things he has targeted in his laptop computer. The captain announces that the ship is
sinking at the rate of one floor per 2 minutes. During the trip, Lupin has installed a special
climbing machine in a vertical duct that allow him to get to any of the passenger floor very
fast. However, provided that the floor is still dry when he reaches the floor, it will take him 2
minutes to go from any position in the duct into any floor, run to the targeted valuable thing,
grab it and return to the duct, even while water is filling up the floor.

The water will just reach the bottom floor right when Lupin starts his stealing. Lupin has to
plan on which valuable things he can take. Lupin is keen on computer programming and he
has a good idea. He quickly creates a program that helps him decide which valuable thing he
has to go for at each two minutes, in such a way that the sum of values he takes will be the
maximum possible.

Write a program that determine such the maximum possible total value that Lupin can take.

INPUT:
1st line : the number of floors n, 10 ≤ n ≤ 1000
Each of the following 𝑛 lines represents each floor from the top down to the bottom. Each
line contains a list of integers representing values of things in the respective floor. There
are at most 1000 valuable things in each floor. The value of each thing is at most $10000.
OUTPUT: The maximum total value that Lupin can take.

EXAMPLE
INPUT
5
4 46 56
44 52 29
29 25 54 2 55 30
11 20 46 33 11 5
29 5 18 51 15 68

OUTPUT
285

Note: the bold values are taken by Lupin

'''

from disjointsets3 import DisjointSets

def kruskals_with_disjoint_sets(n, edges):
    # Sort the edges based on the cost
    edges.sort(key=lambda x: x[2])

    # Initialize the DisjointSets
    ds = DisjointSets(n)

    # This will store the total cost of the MST
    total_cost = 0

    # Kruskal's algorithm: iterate over edges in ascending order and add them to the MST if they don't form a cycle
    for i, j, cost in edges:
        if ds.findset(i) != ds.findset(j):
            ds.union(i, j)
            total_cost += cost

    return total_cost

# Read the input
n, m = map(int, input().split())
edges = []
for _ in range(m):
    i, j, cost = map(int, input().split())
    edges.append((i, j, cost))

min_cost = kruskals_with_disjoint_sets(n, edges)
print(min_cost)


""""The specific words in the problem that directly suggest using Kruskal's algorithm with Disjoint-Set data structures aren't explicitly mentioned. However, the problem description provides clues that point towards this approach:

1. **Minimum Cost Spanning Tree (MST):**  The problem asks to find the **minimum possible cost** to connect all cities to the capital with **high-speed lines**. This directly translates to finding an MST for the given network of cities and edges (high-speed lines) representing their connections.

2. **Redundant Connections:** The problem mentions that building **all** candidate lines is unnecessary. We need to find a minimal set of connections that connect everything. This again aligns with the concept of an MST, where we aim to connect all nodes with minimal edges.

3. **No Cycles:** Although not explicitly stated, the problem requires a path from each city to the capital. In an MST, there are no cycles, ensuring a single path exists between any two connected nodes.

While the problem doesn't use the exact terms "Kruskal's algorithm" or "Disjoint-Set," the focus on minimizing cost, avoiding redundant connections, and establishing a path from each city to the capital implies that Kruskal's with Disjoint-Sets is a suitable solution due to its ability to achieve these goals efficiently.
"""
