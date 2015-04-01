from stuff.primes import is_prime_naive

def nth_prime(n):
	i = 1
	p = 2
	while i < n:
		p += 1
		if(is_prime_naive(p)):
			i += 1

	return p

print(nth_prime(10001))
