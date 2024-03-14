'''
[10 Marks] Optimal Fleet Management

A logistic company is looking to optimize its fleet of delivery trucks to minimize fuel consumption across different routes.
The company operates several types of trucks, each with a different fuel efficiency rating (measured in miles per gallon) and a maximum load capacity.
Each route has a specific distance and a total load that needs to be transported.
The company wants to assign the most fuel-efficient truck available to each route without exceeding any truck's load capacity.

Given the specifications of each truck in the fleet, the details of each route, and the constraint that each truck can only be assigned to one route, develop a Python program that calculates the minimum total fuel consumption for completing all routes.

INPUT:

The first line contains an integer T (1 ≤ T ≤ 100), the number of trucks.
The next T lines each contain two integers F and L, representing the fuel efficiency (in miles per gallon) and load capacity (in pounds) of each truck, respectively.
The next line contains an integer R (1 ≤ R ≤ 100), the number of routes.
The next R lines each contain two integers D and M, representing the distance (in miles) and total load (in pounds) of each route, respectively.
OUTPUT:

A single number representing the minimum total fuel consumption (in gallons, rounded to 2 decimal places) to complete all routes, or Impossible if it's not possible to assign trucks to all routes without exceeding their load capacities.
EXAMPLE

INPUT:

3
10 1000
15 800
20 600
3
100 500
150 700
200 300
OUTPUT:

33.33
Elaboration:

The first route (100 miles, 500 pounds) is assigned to the third truck (20 mpg, 600 pounds capacity), consuming 5 gallons.
The second route (150 miles, 700 pounds) is assigned to the first truck (10 mpg, 1000 pounds capacity), consuming 15 gallons.
The third route (200 miles, 300 pounds) is assigned to the second truck (15 mpg, 800 pounds capacity), consuming 13.33 gallons.
The total fuel consumption is 5 + 15 + 13.33 = 33.33 gallons.

This problem invites a combination of sorting, matching, and optimization strategies, encouraging a thoughtful approach to resource allocation under specific constraints.
'''
def min_fuel_consumption(trucks, routes):
    # Sort trucks by fuel efficiency in descending order
    trucks.sort(key=lambda x: (-x[0], x[1]))
    # Sort routes by load in descending order to try matching heavy loads with suitable trucks first
    routes.sort(key=lambda x: -x[1])

    total_fuel = 0
    used_trucks = [False] * len(trucks)

    for d, m in routes:
        for i, (f, l) in enumerate(trucks):
            if not used_trucks[i] and l >= m:
                total_fuel += d / f
                used_trucks[i] = True
                break
        else:
            return "Impossible"

    return round(total_fuel, 2)

# Example input
T = int(input())
trucks = [tuple(map(int, input().split())) for _ in range(T)]
R = int(input())
routes = [tuple(map(int, input().split())) for _ in range(R)]

print(min_fuel_consumption(trucks, routes))
