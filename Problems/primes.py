def primes(n):
	prime = [True] * (n+1)
	p = 2
	while p * p <= n:
		if prime[p] == True:
			for i in range(p * 2, n+1, p):
				prime[i] = False
		p += 1
	res = []
	for i in range(len(prime)):
		if prime[i] == True:
			res.append(i)
	return res





n = 500
print primes(n)