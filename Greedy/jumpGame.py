'''
55. Jump Game
Medium

Topics
Companies
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
'''



# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        reachable = 0
        for i, length in enumerate(A):
            if i > reachable:
                break
            reachable = max(reachable, i + length)
        return reachable >= len(A) - 1


# index = list(map(int, input().split()))
nums = [3,2,1,0,4]
nums2 = [2,3,1,1,4]
solution_instance = Solution()
result = solution_instance.canJump(nums)
result2 = solution_instance.canJump(nums2)

# Print the result
print(result,result2)
