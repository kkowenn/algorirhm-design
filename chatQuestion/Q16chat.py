'''
[10 Marks] The Goblin's Coin Conundrum

In Gringotts Wizarding Bank, a particularly clever goblin banker has devised a new security measure for the vaults.
Each vault has a magical lock that requires the guest to pay a specific amount of Galleons.
However, the catch is that the vault only accepts coins in a sequence that follows the Goblin's peculiar rule: each subsequent coin must be of lesser value than the previous one,
but not less than half of its value.

Given a list of available Galleon denominations which Gringotts accepts (not necessarily in descending order)
and the exact amount needed to unlock a vault,
assist a group of Hogwarts students to determine the minimum number of Galleons required to unlock the vault while following the Goblin's rule.

INPUT:

The first line contains an integer D (1 ≤ D ≤ 100), the number of Galleon denominations that Gringotts accepts.
The second line contains D integers, representing the value of each Galleon denomination.
The third line contains an integer A (1 ≤ A ≤ 10^6), the exact amount of Galleons needed to unlock the vault.
OUTPUT:

A single integer representing the minimum number of Galleons required to unlock the vault.
If it's impossible to unlock the vault due to the Goblin's rule, output Impossible.
EXAMPLE

INPUT:

5
1 4 3 2 5
7
OUTPUT:

2
Elaboration:
The students can pay 5 Galleons first, following the largest denomination possible, and then pay 2 Galleons to make the exact amount of 7. They must choose denominations carefully to ensure they can continue to pay subsequent amounts according to the rule.

This problem is more complex than a typical coin change problem due to the additional constraint of each coin's value in relation to the last. It requires a greedy strategy that also looks ahead to ensure that the rule can continue to be satisfied.
'''

def min_galleons(denominations, amount):
    denominations.sort(reverse=True)
    count = 0
    current_amount = amount

    for coin in denominations:
        if current_amount >= coin:
            # We can use this coin, now let's see how many of them we can use
            num_coins = current_amount // coin
            count += num_coins
            current_amount -= coin * num_coins
            # The next coin must be at least half the value of the current one
            half_coin = coin // 2
            denominations = [d for d in denominations if d <= half_coin]

    if current_amount != 0:
        return "Impossible"

    return count

# Example input processing
D = int(input())
denominations = list(map(int, input().split()))
A = int(input())

print(min_galleons(denominations, A))
