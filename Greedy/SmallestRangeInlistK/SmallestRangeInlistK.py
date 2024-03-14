'''
632. Smallest Range Covering Elements from K Lists
Hard

Topics
Companies
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.



Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]


Constraints:

nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-105 <= nums[i][j] <= 105
nums[i] is sorted in non-decreasing order.
'''
'''
import heapq


class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        left, right = float("inf"), float("-inf")
        min_heap = []
        for row in nums:
            left = min(left, row[0])
            right = max(right, row[0])
            it = iter(row)
            heapq.heappush(min_heap, (next(it, None), it))

        result = (left, right)
        while min_heap:
            (val, it) = heapq.heappop(min_heap)
            val = next(it, None)
            if val is None:
                break
            heapq.heappush(min_heap, (val, it))
            left, right = min_heap[0][0], max(right, val)
            if right - left < result[1] - result[0]:
                result = (left, right)
        return result
'''

from simplePriorityQueue import Simple_Priority_Queue

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        left, right = float("inf"), float("-inf")
        min_heap = Simple_Priority_Queue()  # Use Simple_Priority_Queue instead of heapq
        for row in nums:
            left = min(left, row[0])
            right = max(right, row[0])
            it = iter(row)
            min_heap.enqueue((next(it, None), it))  # Enqueue tuple (value, iterator)

        result = (left, right)
        while not min_heap.empty():
            (val, it) = min_heap.dequeue()
            val = next(it, None)
            if val is None:
                break
            min_heap.enqueue((val, it))
            left, right = min_heap.a[0][0], max(right, val)
            if right - left < result[1] - result[0]:
                result = (left, right)
        return result

solution = Solution()
nums1 = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
nums2 = [[1,2,3],[1,2,3],[1,2,3]]

print(solution.smallestRange(nums1))
print(solution.smallestRange(nums2))


