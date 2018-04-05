# Given two strings, compute the edit distance between them.

def edit_distance(a, b):
	store = {}
	res = 0
	for char in a:
		if char not in store:
			store[char] = 1
		else:
			store[char] += 1

	for char in b:
		if char not in store or store[char] == 0:
			res += 1
		else:
			store[char] -= 1

	return res




a = "kitten"
b = "sitting"

print edit_distance(a, b)