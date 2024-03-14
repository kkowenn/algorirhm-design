'''
[10 Marks] Typing jobs

Somchai needs to finish typing a lot of documents during this weekend. Contents of all the
documents are well prepared and drafted but need to be typed beautifully in a word
processor. There are exactly N number of documents to be submitted to his boss on Saturday
night and another N number of documents to be submitted on Sunday night. Realizing he
cannot himself type all the documents on time, he decides to hire N number of professional
typists to type the documents for him.

So each typist needs to type one document on Saturday and another one on Sunday. Of
course, each document has different number of pages to be typed. Somchai will pay each
typist minimum of 2,000 Baht for the two days of typing work. However, if the total number
of pages a typist needs to type during the two days exceeds T pages, he will pay the typist
extra R Baht per page for each extra page after the first T pages. Somchai wishes to minimize
the extra payments he may have to make for the extra pages of typing.

Somchai needs to find a way of assigning each typist one Saturday typing job and one
Sunday typing job so that total extra payments he may have to make is minimized.

INPUT:
1st line: Three integers 1 <= N <= 100, 1 <= T <= 10000, and 1 <= R <= 10, as described
above, in the order given, separated by white space.
2nd line: N positive integers separated by a white space, each integer (guaranteed to be <=
10000) denoting the number of pages to be typed for each typing job to be done
on Saturday. (The integers are NOT in any particular order)
3rd line: N positive integers separated by a white space, each integer (guaranteed to be <=
10000) denoting the number of pages to be typed for each typing job to be done
on Sunday. (The integers are NOT in any particular order)

OUTPUT:
A single line of output containing an integer denoting the minimum possible extra payments
Somchai must pay.

EXAMPLE

INPUT
2 30 5
20 15
15 20
OUTPUT
50

INPUT
3 400 10
40 20 30
50 80 30
OUTPUT
0

INPUT
3 5 1
1 4 7
3 1 2
OUTPUT
4
'''


n, t, r = list(map(int, input().split()))
sat = list(map(int, input().split()))
sun = list(map(int, input().split()))

over = 0
remain = 0

for i in range(len(sat)):
    numPaper = sat[i] + sun[i]
    numPaper -= t
    if numPaper >= 1:
        over += numPaper
    else:
        remain += abs(numPaper)

result = abs(over - remain)*r
print(result)

"""
 While the problem doesn't explicitly mention specific algorithms by name, it does provide clues suggesting a combinatorial optimization approach, likely a matching algorithm or a variation thereof:

1. **Pairing Typists and Jobs:** The problem involves optimally pairing `N` typists with `N` Saturday jobs and `N` Sunday jobs to minimize extra payments. This pairing requirement hints at a matching problem.

2. **Total Cost Minimization:** The goal is to minimize the total extra payments, suggesting an optimization objective.

3. **Assignment Constraints:** Each typist must be assigned exactly one Saturday job and one Sunday job, forming specific matching constraints.

4. **No Inherent Ordering:** The jobs aren't ordered in any particular way, indicating that the priority is finding optimal pairs, not a specific sequence.

5. **Discrete Values:** The number of typists, jobs, and pages are all discrete values, aligning with combinatorial optimization approaches.

While the exact algorithm isn't specified, the focus on pairing, optimization, and matching constraints suggests a matching algorithm as a promising solution strategy for this problem.

"""
