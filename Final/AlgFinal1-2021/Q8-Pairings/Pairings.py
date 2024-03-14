'''
 Pairings For The Best Chance to Win

A university tennis team is pairing up for traditional inter-collegiate mixed-double event. A
mixed-double match features a pair of tennis players competing against another pair, in
which each pair comprises one male and one female tennis player.

In this traditional event, 𝑛 matches will be played, simultaneously in 𝑛 tennis courts.
Therefore, each team must line up 𝑛 mixed double pairs.

There is no information about how the line-up of the opposing team will be, therefore the
coach can only try to maximize the chance of winning. He has the records of every pairing of
his selected 𝑛 male players and 𝑛 female players. So he graded every pairing with a rating
system; the lower rating value indicates the pair the won more, while the higher rating
indicates the pair that lost more.

With the complete table of every pairing, the coach would like to determine the best possible
pairings of the entire team. He defines such pairings as the one that has the minimum sum of
the ratings of all the selected 𝑛 pairs.

Write a program to determine the minimum possible sum of ratings for this university team.

Input:
1st line : the number of pairings required, 𝑛, 3 ≤𝑛≤17
Each of the following 𝑛 lines consists of positive 𝑛 integers in fixed order. Thus, these 𝑛
lines form an 𝑛×𝑛 matrix, 𝐴, which describes pairings of 𝑛 male players with 𝑛 female
players. The element in column 𝑗 of row 𝑖, denoted 𝐴𝑖𝑗, is the rating of pairing female
player 𝑖 with male player 𝑗.
Output: Minimum possible sum of ratings for 𝑛 mixed-double pairings.

EXAMPLE

INPUT
4
4 3 2 1
5 5 1 4
2 1 3 4
2 3 1 4

OUTPUT
5

Note: the selected 4 pairings are indicated with the bold numbers.
1 + 1 + 1 + 2 = 5
'''

def find_minimum_assignment(matrix, n, female, used_male, current_sum):
    # If all female players are assigned, return the current sum
    if female == n:
        return current_sum

    # Variable to keep track of the minimum sum
    min_sum = float('inf')

    # Try assigning the current female player to each male player
    for male in range(n):
        # Only assign if the male player is not already used
        if not used_male[male]:
            used_male[male] = True
            # Choose the current male player and move to the next female player
            temp_sum = find_minimum_assignment(matrix, n, female + 1, used_male, current_sum + matrix[female][male])
            # If the new sum is smaller than the current minimum, update it
            if temp_sum < min_sum:
                min_sum = temp_sum
            # Backtrack: un-choose the current male player
            used_male[male] = False

    return min_sum

# Read the input
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Initialize the used_male list to keep track of which male players have been assigned
used_male = [False] * n

# Calculate the minimum sum of ratings
min_sum = find_minimum_assignment(matrix, n, 0, used_male, 0)

print(min_sum)
