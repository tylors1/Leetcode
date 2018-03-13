import time


def isHappy(n):
	
	if n == 1:
		return True
	a = set()
	while n not in a:
		a.add(n)
		total = 0
		if n == 1:
			return True
		for num in str(n):
			total += int(num) ** 2
		print total
		print a
		n = total

	return False







n = 2
print isHappy(n)