from operator import mul
from itertools import combinations

numbers_with_3_digits = range(100,1000)
max_product = 0

for nums in combinations(numbers_with_3_digits, 2):
	product = reduce(mul, nums)
	if product != int(str(product)[::-1]):
		continue

	max_product = max([product, max_product])

print(max_product)
