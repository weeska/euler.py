import glob
import pickle
import re

from primes import prime_sieve, is_prime_naive

#TODO: refactor
#TODO: return primes to n even if more primes are cached

def primes_until_n_cached(n):
	regExp = re.compile(r"(\d+)")
	files = sorted(glob.glob("primes_cache_*.txt"))

	maxCached = 0
	for f in files:
		match = regExp.search(f)
		if match and int(match.group()) > maxCached:
			maxCached = int(match.group())

	primes = []
	if maxCached > 0:
		primes = pickle.load(open("primes_cache_%s.txt" % maxCached, "rb"))
		print("Continuing at %s" % maxCached)

	if maxCached >= n:
		return primes

	for k in range(maxCached + 1, n + 1):
		if is_prime_naive(k):
			primes.append(k)

	pickle.dump(primes, open("primes_cache_%s.txt" % n, "wb+"))

	return primes
