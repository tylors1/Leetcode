def climbStairs(n):
	a = 1
	b = 0

	for i in range(n):
		a, b = a + b, a
	return a

n = 5
print climbStairs(n)