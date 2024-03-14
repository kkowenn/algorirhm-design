class Solution:
    def countOfPairs(self, n, x, y):
        mi = min(x, y) - 1
        ma = max(x, y) - 1
        res = [0] * n
        for i in range(n - 1):
            for j in range(i + 1, n):
                dis = min(j - i, abs(mi - i) + abs(ma - j) + 1)
                res[dis - 1] += 2
        return res

n, x, y  = map(int, input().split())
solution = Solution()
result = solution.countOfPairs(n,x,y)

print(result)
