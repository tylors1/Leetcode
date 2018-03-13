def twopairs(a, k):
	result = 0
	if len(a) < 2:
		return False
	a_dict = {}
	for i in range(len(a)):
		if a[i] in a_dict:
			result += 1
		else:
			a_dict[k - a[i]] = i
	return result

print twopairs([6, 6, 3, 9, 3, 5, 1], 12)