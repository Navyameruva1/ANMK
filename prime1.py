def is_prime(num):
    """
    Checks if a given number is prime.
    A number is prime if it is greater than 1 and has no positive divisors other than 1 and itself.
    """
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # If divisible by any number other than 1 and itself, it's not prime
    return True  # If no divisors found, it's prime

prime_numbers = []
for number in range(1, 101):
    if is_prime(number):
        prime_numbers.append(number)

print("Prime numbers between 1 and 100 are:")
print(prime_numbers)