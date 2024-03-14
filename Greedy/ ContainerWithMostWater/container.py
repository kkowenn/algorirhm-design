class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea

# Input values as a list
height = list(map(int, input().split()))

# Create an instance of the Solution class
solution_instance = Solution()

# Call the maxArea method
result = solution_instance.maxArea(height)

# Print the result
print(result)
