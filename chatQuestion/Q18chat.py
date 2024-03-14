'''
[10 Marks] Wizarding Investments in Diagon Alley

Patrick Ollivander, a savvy wizard investor in Diagon Alley, is looking to invest in shops to support the magical community.
He believes in the future of wizarding commerce and has decided to put his Galleons to good use. Patrick has a list of shops he considers promising,
each with its current investment cost and predicted profit over a year after considering the effects of magical fluctuations.

Help Patrick invest his Galleons to maximize his annual profit. Due to magical laws of commerce, once he invests in a shop
, he must invest the full amount requested by the shop owner, and he cannot invest in more than a certain number of shops to avoid a monopoly.

INPUT:

The first line contains 2 integers, G and S (1 ≤ G ≤ 1,000,000,000 and 1 ≤ S ≤ 50), the amount of Galleons Patrick is willing to invest and the number of shops he is considering, respectively.
Each of the following S lines contain two integers, C and P. The first integer C is the cost to invest in the shop (in Galleons), and the second integer P is the predicted profit from that investment after one year (in Galleons).
OUTPUT:

The maximum total profit Patrick can earn in one year. If he does not have enough Galleons to invest in the minimum number of shops required by magical commerce laws, output Not enough Galleons.
EXAMPLE

INPUT:

100 3
50 60
70 80
30 40
OUTPUT:

120
Elaboration:
Patrick decides to invest in the first and third shops. The total cost is 50 + 30 = 80 Galleons, and the total profit he will earn after one year is 60 + 40 = 100 Galleons. The second shop would overextend his budget of 100 Galleons, so he cannot invest in it.

'''

class ShopInvestment:
    def __init__(self, cost, profit):
        self.cost = cost
        self.profit = profit
        self.ratio = profit / cost

def max_annual_profit(G, shops):
    # Sort the shops by profit-to-cost ratio in descending order
    shops.sort(key=lambda x: x.ratio, reverse=True)

    total_cost = 0
    total_profit = 0
    for shop in shops:
        if total_cost + shop.cost <= G:
            total_cost += shop.cost
            total_profit += shop.profit
        else:
            # If not enough Galleons for this shop, continue to the next
            continue

    # Check if the minimum number of shops has been invested in
    if total_cost < G:
        return "Not enough Galleons"

    return total_profit

# Input processing
G, S = map(int, input().split())
shops = []

for _ in range(S):
    cost, profit = map(int, input().split())
    shops.append(ShopInvestment(cost, profit))

# Calculate and print the result
print(max_annual_profit(G, shops))
