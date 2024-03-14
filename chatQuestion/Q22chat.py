'''
Optimal Path with Discounts

In a city, there are n intersections connected by m bidirectional roads.
Each road has a toll cost associated with it. A traveler is planning to move from intersection 1 to intersection n and has a coupon that can be used to halve the toll cost of any one road along their path.
The goal is to determine the minimum total cost of reaching intersection n from intersection 1, taking into account the optimal use of the coupon.

INPUT:

The first line contains two integers, n (1 ≤ n ≤ 1000) and m (1 ≤ m ≤ 2000), representing the number of intersections and roads, respectively.
Each of the next m lines contains three integers u, v, and c (1 ≤ u, v ≤ n, 1 ≤ c ≤ 1000), indicating that there is a road between intersections u and v with a toll cost of c.
OUTPUT: The minimum total cost of reaching intersection n from intersection 1, using the coupon optimally.

EXAMPLE

INPUT

4 4
1 2 3
2 3 5
3 4 2
1 3 10
OUTPUT

7
Elaboration:

One optimal path is 1 → 2 → 3 → 4. Without the coupon, the total cost is 3 + 5 + 2 = 10. If the coupon is used on the road between intersections 2 and 3,
halving the cost from 5 to 2.5 (assume you can handle decimal or just take the floor value after halving), the total cost becomes 3 + 2.5 + 2 = 7.5,
which rounds to 7 assuming we take floors after applying the coupon.

This problem asks for a strategic application of a discount to minimize total costs, taking into consideration the structure of the network and
the costs associated with traversing it.

Solution Approach:
This problem can be approached using a modified Dijkstra's algorithm or a dynamic programming strategy to find the shortest path while considering the use of the coupon on each road.
You'll need to maintain the state of whether the coupon has been used in your path calculations.
'''

from simplePriorityQueue import Simple_Priority_Queue

def compare_tuples(x, y):
    return x[0] < y[0]

def dijkstra_with_discount(n, m, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v, c in edges:
        graph[u].append((v, c))
        graph[v].append((u, c))

    distances = [[float('inf'), float('inf')] for _ in range(n + 1)]
    distances[1][0] = 0

    queue = Simple_Priority_Queue(compare_tuples)
    queue.enqueue((0, 1, False))

    while not queue.empty():
        cost, node, used_coupon = queue.dequeue()

        if node == n:
            break

        for neighbor, toll_cost in graph[node]:
            new_cost = cost + toll_cost
            if new_cost < distances[neighbor][used_coupon]:
                distances[neighbor][used_coupon] = new_cost
                queue.enqueue((new_cost, neighbor, used_coupon))

            if not used_coupon:
                new_cost_with_coupon = cost + toll_cost // 2
                if new_cost_with_coupon < distances[neighbor][True]:
                    distances[neighbor][True] = new_cost_with_coupon
                    queue.enqueue((new_cost_with_coupon, neighbor, True))

    return min(distances[n])

def bfs_with_discount(n, m, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v, c in edges:
        graph[u].append((v, c))
        graph[v].append((u, c))

    visited = [[False, False] for _ in range(n + 1)]
    visited[1][0] = True

    queue = Simple_Priority_Queue()
    queue.enqueue((0, 1, False))  # Cost, Node, Used_coupon

    while not queue.empty():
        cost, node, used_coupon = queue.dequeue()

        if node == n:
            return cost

        for neighbor, toll_cost in graph[node]:
            next_cost = cost + toll_cost
            if not visited[neighbor][used_coupon]:
                visited[neighbor][used_coupon] = True
                queue.enqueue((next_cost, neighbor, used_coupon))

            if not used_coupon and not visited[neighbor][1]:
                visited[neighbor][1] = True
                queue.enqueue((cost + toll_cost // 2, neighbor, True))

    return -1


# Example input
n, m = 4, 4
edges = [
    (1, 2, 3),
    (2, 3, 5),
    (3, 4, 2),
    (1, 3, 10)
]

# Calculate and print the minimum total cost
print(dijkstra_with_discount(n, m, edges))
# Calculate and print the minimum total cost
print(bfs_with_discount(n, m, edges))
