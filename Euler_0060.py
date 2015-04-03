from itertools import combinations
from stuff.primes import is_prime_naive, prime_sieve

def are_quite_remarkable(nums):
	for x in nums:
		for y in nums:
			if x == y:
				continue

			pq = int("".join([str(x), str(y)]))
			if not is_prime_naive(pq):
				return False
	
	return True

def combinations_tuple(iterable, n):
	for comb in combinations(iterable, n):
		yield list(comb)

def result():
	primes = list(prime_sieve(1000))
	num_primes = len(primes)
	for a in range(num_primes):
		for b in range(a + 1, num_primes):
			for c in range(b + 1, num_primes):
				for d in range(c + 1, num_primes):
						nums = [primes[a], primes[b], primes[c], primes[d]]
						if are_quite_remarkable(nums):
							return sum(nums), nums

print( result() )