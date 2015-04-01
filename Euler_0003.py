def factors(n):
	k = 2
	while n > 1:

		if n % k == 0:
			n /= k
			yield k
			k = 2
		else:
			k += 1

print max(factors(600851475143))
