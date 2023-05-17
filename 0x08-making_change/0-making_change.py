#!/usr/bin/python3
"""
    A function to determine the fewest number of coins needed
    to meet a given total
"""

def makeChange(coins, total):
    """
    This function will take a list of coins and then
    calculate how much change the total will require
    """
    
    if total <= 0:
        return 0

    else:
        sort = sorted(coins, reverse=True)
        counter = 0
        for i in range(len(sort)):
            while (total >= sort[i]):
                counter += 1
                total -= sort[i]
    if total == 0:
        return counter
    return -1
