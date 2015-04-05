from itertools import count

nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

def is_divisible_by_1_to_20(p):
	return all(p % q == 0 for q in nums)

for n in count(20, 20):
	print(n)
	if is_divisible_by_1_to_20(n):
		print(n)
		break