"""
input: [5, 7, 1, 1, 2, 3, 22]
output: 20
"""

# o(nlogn) in time | o(1) in space
def nonConstructibleChange(coins):
    # Write your code here.
    current_max = 0
    coins.sort()
    for i in range(len(coins)):
        cc = coins[i]
        if cc > current_max + 1:
            return current_max + 1
        else:
            current_max += cc
    return current_max + 1
