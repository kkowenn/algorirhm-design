"""
135. Candy
Hard

Topics
Companies
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.



Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.


Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.


Constraints:

n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 10
"""
# Time:  O(n)
# Space: O(n)

class Solution1(object):
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        candies = [1 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in reversed(range(1, len(ratings))):
            if ratings[i - 1] > ratings[i] and candies[i - 1] <= candies[i]:
                candies[i - 1] = candies[i] + 1

        return sum(candies)

# Time:  O((R * C)^2)
# Space: O(1)

class Solution2(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        R, C = len(board), len(board[0])
        changed = True

        while changed:
            changed = False

            for r in range(R):
                for c in range(C-2):
                    if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                        board[r][c] = board[r][c+1] = board[r][c+2] = -abs(board[r][c])
                        changed = True

            for r in range(R-2):
                for c in range(C):
                    if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                        board[r][c] = board[r+1][c] = board[r+2][c] = -abs(board[r][c])
                        changed = True

            for c in range(C):
                i = R-1
                for r in reversed(range(R)):
                    if board[r][c] > 0:
                        board[i][c] = board[r][c]
                        i -= 1
                for r in reversed(range(i+1)):
                    board[r][c] = 0

        return board

prices1 =  [1,0,2]
prices2 =  [1,2,2]

solution_instance = Solution1()
result1 = solution_instance.candy(prices1)
result2 = solution_instance.candy(prices2)
print(result1, result2)

'''
solution_instance = Solution2()
result1 = solution_instance.candyCrush(prices1)
result2 = solution_instance.candyCrush(prices2)
print(result1, result2)
'''
