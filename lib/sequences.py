#!/usr/bin/env python3
#code starts here

def print_fibonacci(n):
    """Prints a list of the Fibonacci sequence up to the length provided."""
    if n <= 0:
        print([])  # For non-positive values, return an empty list
        return
    
    # Initialize the first two numbers in the Fibonacci sequence
    fib_sequence = [0, 1]
    
    # Generate the Fibonacci sequence up to the required length
    while len(fib_sequence) < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    
    # Print the Fibonacci sequence up to length n
    print(fib_sequence[:n])
