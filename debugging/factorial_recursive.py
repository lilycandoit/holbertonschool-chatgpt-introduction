#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.

    Parameters:
    n (int): A non-negative integer for which to compute the factorial.

    Returns:
    int: The factorial of n. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read number from command line and compute factorial
f = factorial(int(sys.argv[1]))
print(f)
