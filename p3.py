import math

def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n."""
    while n % 2 == 0:
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            n //= f
    return n

if __name__ == "__main__":
    num = 600851475143
    print(largest_prime_factor(num))  # -> 6857
