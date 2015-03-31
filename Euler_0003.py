from stuff.primes import is_prime_naive

def prime_factors(n):
	k = 2
	while n > 1:

		if n % k == 0 and is_prime_naive(k):
			n /= k
			yield k
			k = 2
		else:
			k += 1

print max(prime_factors(600851475143))
