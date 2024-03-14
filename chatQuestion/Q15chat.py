'''
[10 Marks] Potion Ingredient Harvesting

Professor Sprout is preparing a large batch of Polyjuice Potion for an undercover mission of the Order of the Phoenix.
The potion requires a careful selection of magical herbs that grow in the Hogwarts greenhouse. Each herb has a potency level and a rarity score.
To make the most effective potion, Sprout needs to harvest the herbs in such a way that the potion's effectiveness, which is the product of potency levels,
is maximized. However, due to the rare nature of some herbs, each subsequent herb harvested must have a rarity score equal to or greater than the last to not deplete any species.

Given a list of magical herbs, their potency levels, and rarity scores, help Professor Sprout determine the order of harvesting to maximize the potion's effectiveness while adhering to the conservation rule.

INPUT:

The first line contains an integer H (1 ≤ H ≤ 1000), the number of herbs in the greenhouse.
Each of the next H lines contains two integers P and R (1 ≤ P ≤ 1000, 1 ≤ R ≤ 1000), representing the potency level and rarity score of each herb.
OUTPUT:

A single number representing the maximum effectiveness of the Polyjuice Potion that can be achieved.
If it's impossible to make the potion due to the rarity conservation rule, output 0.
EXAMPLE

INPUT:

5
4 6
2 9
3 5
7 7
1 10
OUTPUT:

84
Elaboration:
Professor Sprout can select the herbs with potency levels 4 and rarity 6, followed by the herb with potency 7 and rarity 7, to get a potion effectiveness of 4 * 7 = 28.
The remaining herbs cannot be added without breaking the conservation rule (as their rarity scores are not in non-decreasing order).

This problem can be solved with a greedy algorithm that sorts the herbs by rarity score and then selects the highest-potency herbs in compliance with the conservation rule.
'''


def max_potion_effectiveness(herbs):
    # Sort the herbs by rarity score and then by potency level in descending order
    herbs.sort(key=lambda x: (x[1], -x[0]))

    max_effectiveness, current_potency = 0, 0
    for potency, rarity in herbs:
        if potency > current_potency:
            max_effectiveness = max(max_effectiveness, potency)
            current_potency = potency

    return max_effectiveness

# Example input processing
H = int(input())
herbs = [tuple(map(int, input().split())) for _ in range(H)]

print(max_potion_effectiveness(herbs))
