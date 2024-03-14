import time
import sys
sys.setrecursionlimit(10000)

n = int(input())
M = []
for i in range(n):
    x = list(map(int, input().split()))
    x = [a if a >= 0 else 1000000 for a in x]
    M.append(x)

def minM(i, j, k):
    if i >= 0 and j >= 0 and k >= 0:
        if j > 0:
            minM(i, j-1, k)
        if i > 0:
            minM(i-1, j, k)
        if k > 0:
            minM(i,j,k-1)
        x = M[i][k] + M[k][j]
        M[i][j] = min(M[i][j], x)

st = time.process_time()
minM(n-1,n-1,n-1)
et = time.process_time()
print(et-st)

for i in range(n):
    for j in range(n-1):
        print(M[i][j],end=' ')
    print(M[i][n-1])

""""
The problem doesn't explicitly mention any keywords related to dynamic programming. However, it provides clues that suggest this approach is a better fit:

1. **Overlapping Subproblems:**  The problem involves finding the minimum value for each element `M[i][j]`, considering calculations based on elements `M[i][k]` and `M[k][j]`.  These calculations have overlapping subproblems as the same `M[k][j]` value might be used for multiple `M[i][j]` calculations. Dynamic programming excels at handling overlapping subproblems efficiently.

2. **Exponential Time Complexity:** The problem mentions the recursive approach's time limit issue for larger matrices, suggesting an exponential time complexity (O(n^3) in this case). Dynamic programming can achieve the same time complexity (O(n^3)) but with significant optimization by avoiding redundant calculations.

While the problem doesn't use the exact term "dynamic programming," the focus on overlapping calculations and inefficiency of the recursive approach for larger matrices hints towards dynamic programming as a more suitable solution for improved performance.
"""
