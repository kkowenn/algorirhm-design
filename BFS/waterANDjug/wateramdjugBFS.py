class Solution:
    def canMeasureWater(self, jug1Capacity, jug2Capacity, targetCapacity):
        q = [0]
        seen = set()
        steps = [jug1Capacity, -jug1Capacity, jug2Capacity, -jug2Capacity]

        while q:
            cur = q.pop(0)
            for step in steps:
                tot = cur + step
                if tot == targetCapacity:
                    return True
                if tot not in seen and 0 <= tot <= jug1Capacity + jug2Capacity:
                    seen.add(tot)
                    q.append(tot)
        return False

# Example usage
a, b, c = map(int, input().split())
solution = Solution()
result = solution.canMeasureWater(a, b, c)
print(result)
