'''
[10 Marks] Gathering the Lost Artifacts of the Founders

In the magical world of Harry Potter, the Ministry of Magic has embarked on a quest to gather lost artifacts attributed to the founders of Hogwarts. Each artifact has a unique historical importance and a magic intensity level.
To preserve magical harmony, there's a cap on the total magic intensity that a collector can safely handle.

Given a list of artifacts, their historical importance, and magic intensity levels, help the Ministry's top collector determine which artifacts to gather to maximize the total historical importance while staying within the magic intensity limit.

INPUT:

The first line contains 2 integers, I and A (1 ≤ I ≤ 10^6, 1 ≤ A ≤ 200), the maximum magic intensity the collector can handle and the number of available artifacts.
Each of the following A lines contains two integers, H and M. The first integer H is the historical importance rating of the artifact, and the second integer M is the magic intensity level of the artifact.
OUTPUT:

The maximum total historical importance that the collector can gather. If it's not possible to collect any artifacts without exceeding the magic intensity limit, output Collection Impossible.
EXAMPLE

INPUT:

250 4
100 50
200 150
150 100
120 120
OUTPUT:

350
Elaboration:
The collector decides to gather the first and third artifacts. The total magic intensity is 50 + 100 = 150,
which is under the limit of 250. The total historical importance score is 100 + 150 = 250. The second artifact alone would exceed the magic intensity limit, and the fourth one doesn't maximize the historical importance.
'''

class Artifact:
    def __init__(self, importance, intensity):
        self.importance = importance
        self.intensity = intensity

def max_historical_importance(I, artifacts):
    # Dynamic programming approach to solve the 0/1 knapsack problem
    dp = [0] * (I + 1)

    for artifact in artifacts:
        for intensity in range(I, artifact.intensity - 1, -1):
            dp[intensity] = max(dp[intensity], dp[intensity - artifact.intensity] + artifact.importance)

    max_importance = max(dp)

    if max_importance == 0:
        return "Collection Impossible"

    return max_importance

# Input processing
I, A = map(int, input().split())
artifacts = []

for _ in range(A):
    importance, intensity = map(int, input().split())
    artifacts.append(Artifact(importance, intensity))

# Calculate and print the result
print(max_historical_importance(I, artifacts))
