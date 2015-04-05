def factors(n):
	factors = []
	k = 2
	while n > 1:

		if n % k == 0:
			factors.append(k)
			n /= k
			k = 2
		else:
			k += 1

	return factors

def scm(nums):
	common_factors = {}
	for n in nums:
		fs = factors(n)

		for f in fs:
			if not f in common_factors:
				common_factors[f] = 0
			common_factors[f] = max([common_factors[f], sum([1 for x in fs if x == f])])

	result = 1
	for key,value in common_factors.iteritems():
		result *= key**value

	return result

print(scm([11,12,13,14,15,16,17,18,19,20]))