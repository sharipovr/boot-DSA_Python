import math


def prime_factors(n):
    """
    Finds all prime factors of a number.
    
    Args:
        n: The number to factorize
    
    Returns:
        A list of prime factors, ordered from least to greatest
    """
    factors = []
    
    # Step 1: Divide n by 2 as many times as possible
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Step 2: n must be odd now. Loop over odd numbers from 3 to sqrt(n) inclusive
    # Use math.sqrt() and int() to get the integer square root
    sqrt_n = int(math.sqrt(n))
    i = 3
    while i <= sqrt_n:
        # If n can be divided evenly by i, divide and append i
        # Repeat until i can't divide evenly (nested loop behavior)
        while n % i == 0:
            factors.append(i)
            n = n // i
        i += 2  # Only check odd numbers
    
    # Step 3: If n is still greater than 2, it must be prime
    if n > 2:
        factors.append(n)
    
    # Step 4: Return the list (already ordered from least to greatest)
    return factors

