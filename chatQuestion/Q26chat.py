'''
The Branch and Bound technique is a systematic method for solving optimization problems, often used when enumeration of all possible candidates is required.
Unlike other brute force methods, branch and bound builds a search tree incrementally and uses bounds to prune entire subtrees,
thus reducing the search space. It's particularly useful in solving combinatorial optimization problems such as the Traveling Salesman Problem (TSP),
Knapsack Problem, and Integer Linear Programming.

Here's an illustrative problem that can benefit from the branch and bound technique:

Problem: Balanced Partition
You are given a set of integers, and you need to divide it into two subsets such that the absolute difference between the sum of elements in each subset is minimized.
You need to return this minimum absolute difference.

Input:

A list of integers nums.
Output:

The minimum absolute difference between the sums of the two subsets.
Example:

plaintext
Copy code
Input: nums = [1, 6, 11, 5]
Output: 1
Explanation:
The two subsets can be [1, 5, 6] and [11], with sums 12 and 11 respectively. The absolute difference is 1.
Solution Approach using Branch and Bound:
The problem can be approached by generating all possible subsets and calculating the sum of each subset, aiming to minimize the absolute difference of the sums of two subsets. A brute force method would enumerate all subsets, but a branch and bound approach can prune search paths that will not lead to an optimal solution based on the current best solution.

State Space Tree: Initially, every element can either be in subset 1 or subset 2. This creates a binary tree where each level represents a decision for an element, and each node represents a state defined by the elements chosen so far.
Bounding Function: At any node, you can calculate the sum of the elements chosen for both subsets and estimate the best possible solution from this node by optimistically adding the remaining elements to the subset with the smaller sum. If this optimistic estimate is worse than the current best, you can prune this node and its descendants.
Branching: For each element in nums, branch by including it in subset 1 and in another branch, subset 2.
Backtracking and Pruning: While exploring the tree, maintain the minimum absolute difference encountered. Use this value to prune paths that cannot produce a better solution.
Implementing this approach efficiently in code requires careful management of the current state, including the subsets' sums and the elements remaining to be allocated. The challenge lies in the bounding step, where the decision to prune must be made judiciously to avoid omitting potential solutions while minimizing computation on non-promising paths.

Given the complexity of implementing a detailed branch and bound solution and the explanation's focus, a direct code example is extensive and can vary significantly in its specifics, such as how to represent the state, the choice of data structures, and the bounding conditions. For educational purposes, starting with pseudocode and incrementally developing a full solution while testing on simpler cases can be a very effective learning strategy.
'''

def balanced_partition(nums):
    total_sum = sum(nums)
    n = len(nums)
    best_difference = float('inf')

    def dfs(index, current_sum):
        nonlocal best_difference
        if index == n:
            # Calculate the difference of two subsets
            difference = abs((total_sum - current_sum) - current_sum)
            best_difference = min(best_difference, difference)
            return

        # Branching: include the current element in the first subset
        dfs(index + 1, current_sum + nums[index])

        # Branching: exclude the current element from the first subset (it goes to the second subset)
        dfs(index + 1, current_sum)

    dfs(0, 0)
    return best_difference

# Example small case
nums = [1, 6, 11, 5]
print(balanced_partition(nums))

def findMinSubsetSumDifference(arr):
    total_sum = sum(arr)
    n = len(arr)
    half_sum = total_sum // 2

    # Initialize DP table
    dp = [[False for _ in range(half_sum + 1)] for _ in range(n + 1)]

    # Base case: Zero sum is always possible
    for i in range(n + 1):
        dp[i][0] = True

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, half_sum + 1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]

    # Find the largest j such that dp[n][j] is true
    for j in range(half_sum, -1, -1):
        if dp[n][j]:
            return total_sum - 2 * j

# Example usage
arr = [3, 1, 4, 2, 2, 1]  # Smaller case for illustration
print(findMinSubsetSumDifference(arr))
