
a = 1
b = 1
c = a + b
s = 0
while c < 4*10**6:
	s += c
	a = b + c
	b = c + a
	c = a + b

print(s)