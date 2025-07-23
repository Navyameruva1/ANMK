import math

def factorial(n):
    """Calculates the factorial of a non-negative integer."""
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def is_strong_number(num):
    """Checks if a number is a strong number."""
    if num < 0:
        return False
    
    original_num = num
    sum_of_factorials = 0
    
    # Handle the case of 0 separately as 0! is 1, but it's not a strong number in the traditional sense
    if num == 0:
        return False

    while num > 0:
        digit = num % 10
        sum_of_factorials += factorial(digit)
        num //= 10
    
    return sum_of_factorials == original_num

# Iterate through numbers from 1 to 5000 and print strong numbers
print("Strong numbers between 1 and 5000 are:")
for number in range(1, 5001):
    if is_strong_number(number):
        print(number)