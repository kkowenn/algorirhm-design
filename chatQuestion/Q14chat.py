'''
[10 Marks] Dumbledore's Army Training Schedules

Professor Dumbledore is creating a training schedule for Dumbledore's Army (DA). The Room of Requirement offers various magical facilities,
each enabling the DA members to practice different spells. Due to the complex magic of the room, each facility can only be used once before it disappears.
Each DA member has a different aptitude for learning each spell, and Dumbledore wants to maximize the overall proficiency gained.

Given the list of DA members, the facilities in the Room of Requirement, and the proficiency each member can gain by training at each facility,
Dumbledore needs to assign members to the facilities to maximize the total proficiency. A DA member can only use one facility, and once a facility is used,
it cannot be used by another member.

INPUT:

The first line contains an integer M (1 ≤ M ≤ 100), the number of DA members.
The second line contains an integer F (1 ≤ F ≤ 100), the number of facilities in the Room of Requirement.
Each of the next M lines contains F integers, where the j-th integer in the i-th line represents the proficiency points member i can gain by training at facility j.
OUTPUT:

A single integer representing the maximum total proficiency points that DA members can gain.
EXAMPLE

INPUT:
5
4
3 1 2 4
2 3 5 1
1 1 1 1
4 3 2 5
2 2 2 2
OUTPUT:

14

Elaboration:
Dumbledore might assign the members to facilities in a way that maximizes the total proficiency. 
For instance, the first member could train at the fourth facility for 4 points, the second member at the third facility for 5 points, and so forth. 
The goal is to ensure no two members use the same facility and the sum of proficiency points is as large as possible.

This problem resembles an assignment problem which can be solved optimally using the Hungarian Algorithm or 
can be approached using dynamic programming as a variation of the maximum bipartite matching problem.

'''

def max_proficiency(members):
    M, F = len(members), len(members[0])
    # dp[mask] will store the max proficiency for a set of members represented by the mask
    dp = [0] * (1 << M)

    for mask in range(1, 1 << M):
        member_index = bin(mask).count("1") - 1
        for facility in range(F):
            if mask & (1 << facility) == 0:  # Facility not yet taken
                new_mask = mask | (1 << facility)
                dp[new_mask] = max(dp[new_mask], dp[mask] + members[member_index][facility])

    return dp[-1]

# Example input processing
M = int(input())
F = int(input())
members = [list(map(int, input().split())) for _ in range(M)]

print(max_proficiency(members))
