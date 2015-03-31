import math

def prime_sieve(n):
    ints = [x for x in range(2, n)]
    marked_ints = set()

    p = ints[0]
    for p in ints:
        i = 2

        while i*p <= n:
            if i*p in ints and i*p not in marked_ints:
                marked_ints.add(i*p)
            i += 1

    return set(ints) - marked_ints

def is_prime_naive(n):
    if n <= 2:
        return True

    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True