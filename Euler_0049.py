from stuff.primes import is_prime_naive

def result(): # makes return easier
	for a in range(1000, 10000):

		if a == 1487:
			continue

		if not is_prime_naive(a):
			continue

		aDigits = set(str(a))

		for i in range(1, 9001):
			b = a + i
			c = b + i

			if c > 9999:
				break

			bDigits = set(str(b))
			cDigits = set(str(c))

			if not ( aDigits == bDigits == cDigits):
				continue

			if not (is_prime_naive(b) and is_prime_naive(c)):
				continue

			return "%s%s%s" % (a, b, c)

print(result())