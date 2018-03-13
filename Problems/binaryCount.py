def binary_count(s):
	prev = 0
	current = 1
	res = 0
	for i in range(len(s))[1:]:
		if s[i] == s[i-1]:
			current += 1
		else:
			prev = current
			current = 1
		if prev >= current:
			res += 1
	return res



print binary_count("00110")
print binary_count("101010101")
print binary_count("1101110001")