'''
[10 Marks] Optimal Resource Allocation in Automated Factories

In the world of automated manufacturing, factories are equipped with robotic arms that operate in unison to assemble products.
Each robotic arm has a cost efficiency rating, which combines its speed and precision factors.
The factory floor is laid out in a grid, with certain grid points designated as assembly stations.
Each assembly station has a demand for a certain number of robotic arms based on the complexity of tasks performed at that station.

Given the factory grid with assembly stations and their demand, along with a list of available robotic arms with their cost efficiency ratings, 
develop a Python program that allocates robotic arms to maximize the overall cost efficiency while meeting the demand at each assembly station.

INPUT:

The first line contains an integer G (1 ≤ G ≤ 50), the size of the factory grid (GxG).
The next line contains an integer S (1 ≤ S ≤ G²), the number of assembly stations.
Each of the next S lines contains three integers X, Y, and D, representing the coordinates (X, Y) of the assembly station on the grid and its demand D for robotic arms.
The next line contains an integer R (1 ≤ R ≤ 100), the number of available robotic arms.
Each of the next R lines contains an integer E, representing the cost efficiency rating of a robotic arm.
OUTPUT:

A single number representing the maximum total cost efficiency achieved after allocating robotic arms to the assembly stations. 
If it's impossible to meet the demand at all assembly stations with the available robotic arms, print Impossible.
EXAMPLE

INPUT:

5
3
1 1 2
2 3 1
4 4 3
5
100
80
95
90
85
OUTPUT:

450
Elaboration:

The most cost-efficient allocation would assign robotic arms with efficiencies 100 and 95 to the station at (1, 1), 90 to the station at (2, 3), and 85, 80, and another 95 to the station at (4, 4).
The total cost efficiency would be 100 + 95 + 90 + 85 + 80 + 95 = 545.
This question requires an algorithm that not only matches the demands and supplies but also optimizes for the highest total cost efficiency rating. It would likely involve a form of the Knapsack problem or a matching problem like the Assignment problem, which can be solved using algorithms such as the Hungarian method or other optimization techniques.
'''

from itertools import permutations

def allocate_robots(grid_size, stations, robotic_arms):
    # Assume stations and robotic_arms are already sorted by demand and efficiency, respectively.
    # This is a brute force approach, which is not efficient for large inputs. It is just to illustrate the idea.

    max_efficiency = -1
    for perm in permutations(robotic_arms):
        efficiency = 0
        ptr = 0
        for x, y, demand in stations:
            if ptr + demand > len(perm):  # Not enough robots left for this station
                return "Impossible"
            for _ in range(demand):
                efficiency += perm[ptr]
                ptr += 1
        max_efficiency = max(max_efficiency, efficiency)

    return max_efficiency if max_efficiency != -1 else "Impossible"

G = int(input())
S = int(input())
stations = [tuple(map(int, input().split())) for _ in range(S)]
R = int(input())
robotic_arms = [int(input()) for _ in range(R)]

print(allocate_robots(G, stations, robotic_arms))

'''
# Given values for illustration based on the described approach
stations = [(1, 1, 2), (2, 3, 1), (4, 4, 3)]  # Format: (x, y, demand)
robotic_arms = [100, 95, 90, 85, 80, 95]

# Sort stations by demand in descending order
stations.sort(key=lambda x: x[2], reverse=True)

# Sort robotic arms by efficiency in descending order
robotic_arms.sort(reverse=True)

allocated_arms = []
for _, _, demand in stations:
    allocated_arms.extend(robotic_arms[:demand])
    robotic_arms = robotic_arms[demand:]

total_efficiency = sum(allocated_arms)
total_efficiency

'''