'''
Here's a new question that relates to the algorithmic techniques used in the previous questions:

Minimum Resource Allocation

In a resource allocation scenario, you are given n tasks and m resources.
Each task requires a specific amount of resources to complete, and each resource has a cost associated with it.
The goal is to allocate resources to tasks in such a way that the total cost is minimized,
subject to the constraint that the sum of resources allocated to a task meets or exceeds its requirement.
The allocation is fractional, meaning that a portion of a resource can be allocated to a task.

INPUT:

The first line contains two integers, n (1 ≤ n ≤ 100) and m (1 ≤ m ≤ 100), representing the number of tasks and the number of resources, respectively.
The next n lines each contain a single integer r_i (1 ≤ r_i ≤ 1000), which is the amount of resource required for task i.
Following this, m lines each contain two integers c_j and v_j (1 ≤ c_j, v_j ≤ 1000),
representing the cost and volume of resource j, respectively.
OUTPUT: The minimum total cost to satisfy all the task requirements. The output should be rounded to two decimal places.

EXAMPLE

INPUT

3 4
100
200
300
50 100
70 150
80 100
60 200
OUTPUT


260.00
Elaboration:

Allocate 100 units of the fourth resource to the first task (cost = 60), 150 units of the second resource to the second task (cost = 70), and 100 units of the third resource plus 50 units of the first resource to the third task (cost = 80 + 50). The total minimum cost is 260.00.

This question encourages thinking about optimization and the efficient allocation of resources, similar to minimizing costs or maximizing efficiency in the provided examples
'''


def min_resource_allocation(n, m, tasks, resources):
    # Sort resources by cost-to-volume ratio
    resources.sort(key=lambda x: x[0] / x[1])

    total_cost = 0.0

    for task in tasks:
        i = 0
        while task > 0 and i < m:
            cost, volume = resources[i]

            # Calculate the amount of this resource to use
            use_volume = min(task, volume)

            # Update the task requirement, total cost, and resource volume
            task -= use_volume
            total_cost += use_volume * (cost / volume)
            resources[i] = (cost, volume - use_volume)

            # Move to the next resource if this one is depleted
            if resources[i][1] == 0:
                i += 1

    return round(total_cost, 2)

# Example input
n, m = 3, 4
tasks = [100, 200, 300]
resources = [(50, 100), (70, 150), (80, 100), (60, 200)]

# Calculate and print the minimum total cost
print(min_resource_allocation(n, m, tasks, resources))
