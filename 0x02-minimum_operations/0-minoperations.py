#!/usr/bin/python3
""" Minimum Operations Algorithm """


def minOperations(n):
    """
    This functions gets the minimum operations used using prime factors,
    E.g if n = 12, prime factors = [2, 2, 3] when we add the prime factors
    we get the number of operations, in this case 7 operations.
    """
    if n == 1:
        return 0   # This returns 0 if theres only 1 H.
    pf = 2  # Here we start with the lowest prime factor 2
    op = 0  # op Gets the number of operations

    while pf * pf <= n:
        if n % pf == 0:  # This checks for all the prime factors
            op += pf  # adds the factor to operations
            n //= pf  # This divides pf to reduce n for the next iteratio
        else:
            pf += 1   # if the number is not a factor, we increment.
    if n > 1:   # Adds the remaining prime factors of n
        op += n
    return op
