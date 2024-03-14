"""
**[10 Marks] Dynamic Dungeon Descent**

In a video game development project, you are tasked with creating an algorithm for generating and navigating through a dynamically changing dungeon.
The dungeon consists of rooms and corridors connecting these rooms. The hero starts in the entrance room and must find the treasure room as quickly as possible.
However, the dungeon is enchanted and its layout can change: some corridors may close or new ones may open, altering the shortest path dynamically.

The dungeon can be modeled as a graph where rooms are nodes, and corridors are edges connecting these nodes.
The weight of an edge represents the time it takes to traverse the corridor.
At certain intervals, the dungeon layout changes, affecting the weights and connections between nodes.

**Objective:** Develop an algorithm that continuously updates the shortest path from the hero's current room to the treasure room, taking into account the dynamic nature of the dungeon layout.

**INPUT:**
- 1st line: Two integers `N` and `M`, where `N` is the number of rooms (2 ≤ N ≤ 500), and `M` is the initial number of corridors.
- 2nd line: Two integers `S` and `T`, representing the indices of the starting (entrance) room and the treasure room, respectively.
- Next `M` lines: Each line contains three integers `u`, `v`, and `w`, indicating a corridor between rooms `u` and `v` with a traversal time of `w` milliseconds.
- After the initial setup, a line `C` indicates the number of layout changes (1 ≤ C ≤ 100).
- Next `C` lines: Each line starts with an integer `K`, the number of corridors affected by this change. Followed by `K` sets of three integers `u`, `v`, and `w`, where `w` can be `-1` indicating the corridor between `u` and `v` is closed, or a positive integer indicating the new traversal time for the corridor.

**OUTPUT:**
For each layout change, output a line containing the minimum time in milliseconds required to reach the treasure room from the entrance.
If it becomes impossible to reach the treasure room, print `-1`.

**EXAMPLE INPUT:**
```
5 6
0 4
0 1 10
1 2 10
2 4 10
0 3 5
3 4 20
1 3 15
2
3 0 1 -1 1 2 -1 2 4 5
1 3 4 10
```

**EXAMPLE OUTPUT:**
```
25
15
```

**Explanation:**
- Initially, the shortest path is `0 -> 1 -> 2 -> 4` with a time of `30ms`.
- After the first change, the path becomes `0 -> 3 -> 4` with corridors `0 -> 1` and `1 ->2` closed, and `2->4` now takes `5ms`, resulting in a time of `25ms`.
- The second change improves the corridor `3->4` to `10ms`, making the path `0 -> 3 -> 4` take only `15ms`.

This question requires understanding dynamic graphs, shortest path algorithms, and how to efficiently handle changes in graph structure.
"""
# Assuming simplePriorityQueue.py exists and contains the Simple_Priority_Queue class

from simplePriorityQueue import Simple_Priority_Queue

def dijkstra_with_custom_pq(graph, start, target):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = Simple_Priority_Queue(cmp=lambda x, y: x[0] < y[0])
    priority_queue.enqueue((0, start))

    while not priority_queue.empty():
        current_distance, current_vertex = priority_queue.dequeue()

        if current_vertex == target:
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                priority_queue.enqueue((distance, neighbor))

    return distances[target]

def update_graph(graph, changes):
    for u, v, w in changes:
        if w == -1:
            if v in graph[u]: del graph[u][v]
            if u in graph[v]: del graph[v][u]
        else:
            graph[u][v] = w
            graph[v][u] = w
    return graph

# Example usage
graph = {
    0: {1: 10, 3: 5},
    1: {0: 10, 2: 10, 3: 15},
    2: {1: 10, 4: 10},
    3: {0: 5, 4: 20, 1: 15},
    4: {2: 10, 3: 20}
}

start, target = 0, 4

# Calculate the shortest path before any changes
shortest_path_before_changes = dijkstra_with_custom_pq(graph, start, target)
print("Shortest path before changes:", shortest_path_before_changes)

# Apply changes to the graph
changes = [(0, 1, -1), (1, 2, -1), (2, 4, 5), (3, 4, 10)]
graph = update_graph(graph, changes)

# Calculate the shortest path after the changes
shortest_path_after_changes = dijkstra_with_custom_pq(graph, start, target)
print("Shortest path after changes:", shortest_path_after_changes)
