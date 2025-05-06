#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to avoid infinite loop
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <number>")
    else:
        try:
            f = factorial(int(sys.argv[1]))
            print(f)
        except ValueError:
            print("Please provide an integer.")

