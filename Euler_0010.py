from stuff.primes import is_prime_naive

print(sum([x for x in range(2, 2000000 + 1) if is_prime_naive(x)]))
