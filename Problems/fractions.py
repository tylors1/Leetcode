def lcm(x, y):
	greater = max(x, y)
	while True:
		if greater % x == 0 and greater % y == 0:
			res = greater
			break
		greater += 1
	return res

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def add_fractions(a, b):
	denominator = lcm(a[1],b[1])
	num_a = denominator/a[1]*a[0]
	num_b = denominator/b[1]*b[0]

	numerator = num_a + num_b
	gcd1 = gcd(numerator, denominator)

	return [numerator/gcd1, denominator/gcd1]


a = [5,6]
b = [7,8]

print add_fractions(a,b)