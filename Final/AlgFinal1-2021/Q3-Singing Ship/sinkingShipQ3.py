'''
Sinking Ship

Lupin is training himself with simulation of a crisis scenario. This time, the crisis he
simulated is sinking cruise ship.

A gigantic cruise ship is hit an underwater iceburg and is sinking. Water is flooding the bilge
and passengers are evacuating to life boats. Lupin the thief, however, finds this to be the time
that he can take valuable things of others without being caught. He has the map of all the
valuable things he has targeted in his laptop computer. The captain announces that the ship is
sinking at the rate of one floor per 2 minutes. During the trip, Lupin has installed a special
climbing machine in a vertical duct that allow him to get to any of the passenger floor very
fast. However, provided that the floor is still dry when he reaches the floor, it will take him 2
minutes to go from any position in the duct into any floor, run to the targeted valuable thing,
grab it and return to the duct, even while water is filling up the floor.

The water will just reach the bottom floor right when Lupin starts his stealing. Lupin has to
plan on which valuable things he can take. Lupin is keen on computer programming and he
has a good idea. He quickly creates a program that helps him decide which valuable thing he
has to go for at each two minutes, in such a way that the sum of values he takes will be the
maximum possible.

Write a program that determine such the maximum possible total value that Lupin can take.

INPUT:
1st line : the number of floors n, 10 ≤ n ≤ 1000
Each of the following 𝑛 lines represents each floor from the top down to the bottom. Each
line contains a list of integers representing values of things in the respective floor. There
are at most 1000 valuable things in each floor. The value of each thing is at most $10000.
OUTPUT: The maximum total value that Lupin can take.

EXAMPLE
INPUT
5
4 46 56
44 52 29
29 25 54 2 55 30
11 20 46 33 11 5
29 5 18 51 15 68
OUTPUT
285

Note: the bold values are taken by Lupin

'''
x = int(input())
y = []

for i in range(x):
    inp = list(map(int, input().split()))
    y.append(inp)
masterY = y.copy()

total = 0

def findMax(a):
    maxx = []
    for i in a:
        maxx.append(max(i))
    return maxx

def findIndex(a, value):
    maxIndex = []
    for i in range(len(a)):
        if a[i] == value:
            maxIndex.append(i)
    return max(maxIndex)


for i in range(x-1,-1,-1):
    max_each_floor = findMax(masterY)
    maxIndex = findIndex(max_each_floor, max(max_each_floor))
    total += max_each_floor[maxIndex]
    masterY[maxIndex].remove(max(max_each_floor))
    masterY.pop(i)
    # print(masterY)

print(total)



""""
The words directly related to the solution approach aren't explicitly mentioned in the problem, but there are clues that suggest a dynamic programming approach might be suitable. Here's why:

1. **Optimal Substructure:** The problem asks for the maximum total value Lupin can steal. To achieve this, he needs to make optimal choices at each floor (deciding which valuable item to take). The optimal choice at a floor depends on the remaining floors and the items available there. This suggests a potential for breaking down the problem into smaller subproblems and combining their solutions for the overall optimal solution, which is a characteristic of dynamic programming.

2. **Overlapping Subproblems:** While not explicitly stated, there might be overlapping subproblems.  For example, the decision on the best item on floor `n-2` might influence the decision on floor `n-1`, considering the remaining time and accessible floors below. Dynamic programming excels at handling overlapping subproblems efficiently.

3. **Staged Decision Making:** The problem involves making decisions (choosing items) at each floor (stage) based on the current state (remaining time and accessible floors) and maximizing the total value. This staged decision-making structure aligns with the dynamic programming approach.

While the problem doesn't use the exact term "dynamic programming," the focus on optimal choices at each stage, potential overlapping subproblems, and staged decision making hint towards dynamic programming as a potential solution for maximizing the total value stolen by Lupin.
"""
