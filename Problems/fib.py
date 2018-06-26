
cache = {}

def fib(n):
	if n <= 1:
		return 1
	else:
		if n not in cache:
			cache[n] = fib(n-2) + fib(n-1)
		return cache[n]


print fib(200)