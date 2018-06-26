

def combinations(n, c):
	res = []

	def recurse(start, combos):
		if len(combos) == c:
			res.append(combos[:])
			return

		# if start > n:
		if len(combos) + (n - start + 1) < c:
			return

		combos.append(start)
		recurse(start + 1, combos)
		combos.pop()
		recurse(start + 1, combos)


	recurse(1, [])
	return res

c = 2
n = 5

print combinations(n, c)