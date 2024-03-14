'''
[10 Marks] Optimal Server Load Balancing

A data center has N servers, each with different processing capacities.
Due to an upcoming heavy workload, tasks are scheduled to be distributed among these servers.
Each task has a defined load, and for optimal performance, the goal is to minimize the maximum load on any server.

Given a list of server capacities and a list of task loads, develop a Python program that determines
the minimum possible maximum load on any server after all tasks have been allocated optimally.

INPUT:

The first line contains an integer N (1 ≤ N ≤ 1000), the number of servers.
The second line contains N integers, representing the capacities of the servers.
The third line contains an integer M (1 ≤ M ≤ 10000), the number of tasks.
The fourth line contains M integers, representing the loads of the tasks.
OUTPUT:

A single integer representing the minimum possible maximum load on any server after optimal task allocation.
EXAMPLE

INPUT:
3
8 16 8
5
10 10 10 10 10

OUTPUT:
20

Elaboration:
One optimal allocation could be:

Server 1 takes two tasks (10+10=20 load)
Server 2 takes two tasks (10+10=20 load)
Server 3 takes one task (10 load)
The maximum load on any server is thus minimized to 20.

This problem requires balancing loads across servers with varying capacities, ensuring no single server is overwhelmed. The solution involves a mix of sorting, greedy allocation, and potentially binary search to find the optimal maximum load.

'''

def can_distribute(tasks, capacities, max_load):
    # Function to check if all tasks can be distributed such that
    # no server exceeds the max_load
    i = 0  # Task index
    for capacity in capacities:
        current_load = 0
        while i < len(tasks) and current_load + tasks[i] <= min(capacity, max_load):
            current_load += tasks[i]
            i += 1
    return i == len(tasks)  # True if all tasks are distributed

def find_min_max_load(capacities, tasks):
    left, right = max(tasks), sum(tasks)  # Minimum and maximum possible max load
    result = right
    while left <= right:
        mid = (left + right) // 2
        if can_distribute(tasks, capacities, mid):
            result = min(result, mid)
            right = mid - 1
        else:
            left = mid + 1
    return result

# Example usage
N = int(input())
capacities = list(map(int, input().split()))
M = int(input())
tasks = list(map(int, input().split()))

# Sorting tasks to try allocating larger tasks first
tasks.sort(reverse=True)
capacities.sort(reverse=True)

print(find_min_max_load(capacities, tasks))
