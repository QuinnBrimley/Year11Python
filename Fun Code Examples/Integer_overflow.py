def add_with_overflow(a, b):
    # Define the maximum value for a 32-bit signed integer
    MAX_INT = 2**31 - 1
    MIN_INT = -2**31
    
    result = a + b
    
    # Simulate overflow
    if result > MAX_INT:
        result = result - 2**32
    elif result < MIN_INT:
        result = result + 2**32
    
    return result

# Example usage
a = 2**31 - 1  # Maximum positive value for a 32-bit signed integer
b = 1          # Adding 1 should cause an overflow

print(f"Adding {a} and {b} results in overflow: {add_with_overflow(a, b)}")

a = -2**31  # Minimum negative value for a 32-bit signed integer
b = -1      # Subtracting 1 should cause an underflow

print(f"Adding {a} and {b} results in underflow: {add_with_overflow(a, b)}")


"""

Reading first:

https://en.wikipedia.org/wiki/Integer_overflow
https://en.wikipedia.org/wiki/Nuclear_Gandhi

This code simulates 32-bit integer overflow by checking if the result of an addition 
exceeds the maximum or minimum bounds of a 32-bit signed integer and then adjusts 
the result accordingly. When you run this code, you will see that adding 2**31 - 1 
(the maximum positive value for a 32-bit signed integer) and 1 results in 
an overflow, which wraps around to the minimum negative value for a 32-bit signed integer. 
Similarly, adding -2**31 (the minimum negative value for a 32-bit signed integer) 
and -1 results in an underflow, wrapping around to the maximum positive value.


In Python, integer overflow is not typically an issue because Python's int type 
can handle arbitrarily large integers. However, in many 
programming languages (such as C or Java), integers have a fixed size, and 
exceeding this size can result in overflow.

To demonstrate an integer overflow scenario, 
we can simulate the behavior of a fixed-width integer (like a 32-bit integer) 
in Python. Here’s a sample code that illustrates how integer overflow works with 
32-bit integers
"""