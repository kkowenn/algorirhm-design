'''
Task Scheduling with Deadlines and Profits

You are given n tasks, each with a deadline and a profit associated with completing the task by its deadline.
Your goal is to schedule the tasks to maximize the total profit, assuming that each task takes exactly one unit of time to complete and can only be worked on one at a time.
You can only work on a task on or before its deadline, and at most one task can be completed on each day.

Input:

A list tasks where each element is a tuple (deadline, profit). deadline is an integer that represents the deadline of the task (the day by which it needs to be completed),
and profit is the profit gained from completing the task. The deadline is counted from the start day, which is 1.
Output:

The maximum total profit you can achieve by scheduling the tasks appropriately.
Example:

plaintext
Copy code
Input: tasks = [(2, 100), (1, 50), (2, 10), (1, 20), (3, 30)]

Output: 150

Explanation:
Day 1: Complete the task with profit 50.
Day 2: Complete the task with profit 100.
No task can be completed on Day 3 as the tasks left either have deadlines that have passed or are less profitable than the tasks already completed.
Total profit = 50 + 100 = 150.
Constraints:

1 <= n <= 10^4
1 <= deadline, profit <= 10^5
Solution Approach:
A greedy approach works well for this problem. Here's the general idea:

Sort the tasks based on their profits in descending order because you want to prioritize tasks with higher profits.
Use a data structure (e.g., a boolean array) to keep track of the days that are already occupied by a scheduled task.
Starting from the task with the highest profit, try to schedule it as close to its deadline as possible. If the preferred day is already taken, find the closest previous day that is available.
Repeat this process for all tasks, and sum up the profits of the scheduled tasks to get the maximum total profit.
This greedy strategy ensures that you maximize the profit by giving priority to more profitable tasks and scheduling them as close to their deadlines as possible to leave room for other tasks

'''

def schedule_tasks(tasks):
    # Sort tasks by profit in descending order
    tasks.sort(key=lambda x: x[1], reverse=True)

    max_day = max(task[0] for task in tasks)  # Find the latest deadline
    schedule = [-1] * max_day  # Initialize the schedule with -1 (indicating an unscheduled day)

    total_profit = 0
    for deadline, profit in tasks:
        # Try to schedule the task as close to its deadline as possible
        for day in range(deadline - 1, -1, -1):
            if schedule[day] == -1:  # If the day is available
                schedule[day] = profit  # Schedule the task
                total_profit += profit  # Add the profit
                break  # Break the loop after scheduling

    return total_profit

# Example input
tasks = [(2, 100), (1, 50), (2, 10), (1, 20), (3, 30)]
tasks2 = [
    (5, 60),  # Deadline 5, Profit 60
    (2, 100), # Deadline 2, Profit 100
    (1, 15),  # Deadline 1, Profit 15
    (4, 90),  # Deadline 4, Profit 90
    (3, 70),  # Deadline 3, Profit 70
    (2, 30)   # Deadline 2, Profit 30
]

total_profits = schedule_tasks(tasks)
total_profits2 = schedule_tasks(tasks2)
print(f"Total unique paths: {total_profits}")
print(f"Total unique paths: {total_profits2}")

