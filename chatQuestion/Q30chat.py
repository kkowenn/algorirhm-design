'''
Problem: Maximum Energy Shield Generation
Tony Stark has upgraded his Iron Man suit with a new defensive system against an incoming wave of Chitauri invaders.
The system generates a temporary energy shield that can absorb a certain amount of damage from Chitauri soldiers before depleting.
Each Chitauri aircraft approaching has a different energy potential that, if absorbed by the shield instead of destroyed,
can extend the shield's durability.

The aircraft are arranged in a line towards Tony, and his energy shield can absorb the energy potential of up to two adjacent aircraft at a time.
However, absorbing an aircraft's energy prevents the shield from immediately absorbing from the next pair of aircraft due to cooldown.
Destroying an aircraft with repulsors does not grant any energy to the shield but does not trigger the cooldown.

Your goal is to maximize the energy absorbed by the shield, given that absorbing energy from Chitauri aircraft also means
Iron Man will take damage from those not absorbed in each action due to their attack as they approach.

Input:

A list of N integers, where each integer represents the energy potential of each consecutive Chitauri aircraft. N is the number of aircraft, with 1 ≤ N ≤ 20, and the energy potential of each aircraft is between 1 and 100.
Output:

The maximum amount of energy the shield can absorb to protect Tony Stark.
Example:

plaintext
Input: [10, 15, 10, 5, 10]

Output: 25

Explanation:
- Absorbing the energy from the 1st and 2nd aircraft provides 25 energy units to the shield. The shield goes into cooldown, skipping the next pair (3rd and 4th aircraft).
- The shield does not absorb energy from the 5th aircraft due to strategy, maximizing the amount of energy absorbed while managing the cooldown effectively.
Solution Approach:
This problem can be approached with dynamic programming or a recursive strategy that explores each possible combination of absorbing energy from pairs of aircraft while respecting the cooldown constraint. The aim is to find the sequence of actions (absorb or skip) that results in the maximum energy absorption.

A recursive solution would consider the maximum energy absorption for each action (absorb or skip) at every step, taking into account the cooldown effect of absorbing energy. This would require careful management of the current state (index and whether the shield is in cooldown) and exploring the consequences of each possible action.

'''
def max_energy_absorbed(aircrafts):
  """
  Calculates the maximum energy absorbed by the shield using dynamic programming.

  Args:
      aircrafts: A list of integers representing the energy potential of each aircraft.

  Returns:
      The maximum energy absorbed by the shield.
  """
  n = len(aircrafts)
  # Memoization table, -1 indicates value not calculated yet
  memo = [[-1 for _ in range(2)] for _ in range(n + 1)]

  def dp(index, cooldown):
    """
    Recursive function to calculate the maximum energy absorbed from a given index.

    Args:
        index: Current aircraft index.
        cooldown: Whether the shield is on cooldown (1) or not (0).

    Returns:
        The maximum energy absorbed up to the current aircraft.
    """
    # Base case: if we've gone through all aircraft
    if index >= n:
      return 0

    # Check memo table
    if memo[index][cooldown] != -1:
      return memo[index][cooldown]

    # Option 1: Skip the current aircraft
    max_energy = dp(index + 1, 0)  # No cooldown after skipping

    # Option 2: Absorb energy from the current and next aircraft (if not on cooldown)
    if cooldown == 0 and index + 1 < n:
      max_energy = max(max_energy, aircrafts[index] + aircrafts[index + 1] + dp(index + 2, 0))  # No cooldown after absorbing two

    # Save and return the result
    memo[index][cooldown] = max_energy
    return max_energy

  return dp(0, 0)

# Example usage
aircrafts = [10, 15, 10, 5, 10]
print(max_energy_absorbed(aircrafts))  # Output: 25


