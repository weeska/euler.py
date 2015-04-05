def result():

	for a in range(1, 1000):
		for b in range(a + 1, 1001 - a):
			c = 1000 - a - b
			if a*a + b*b == c*c and a + b + c == 1000:
				return a*b*c

print(result())
