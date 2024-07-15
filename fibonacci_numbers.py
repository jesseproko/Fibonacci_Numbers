#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def generate_fibonacci(start_num, count):
    """
    Generate a specified number of Fibonacci numbers starting from a given number.

    Parameters:
    start_num (int): The starting number for the Fibonacci sequence (>= 1).
    count (int): The number of Fibonacci numbers to generate.

    Returns:
    list: A list containing the generated Fibonacci numbers.
    """
    # Initialize the first two Fibonacci numbers
    x = start_num
    y = start_num
    fibonacci_sequence = [x]

    # Generate Fibonacci numbers
    for _ in range(count - 1):
        x, y = x + y, x
        fibonacci_sequence.append(x)

    return fibonacci_sequence

# Input from the user
start_num = int(input("What number would you like to start with (>=1)? "))
count = 10  # You can change this to any number of Fibonacci numbers you want to generate

# Generate and print the Fibonacci sequence
fibonacci_sequence = generate_fibonacci(start_num, count)
print("Fibonacci sequence:", fibonacci_sequence)



# In[ ]:




