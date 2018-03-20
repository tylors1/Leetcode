# https://leetcode.com/problems/custom-sort-string/description/


def customSortString(S, T):

	# iterate through T and count occurances of each char
	# iterate through S, and add to res the number of occuances of each char
	# add remaining elements in store to res


	res = []
	store = {}

	for char in T:
		if not char in store:
			store[char] = 1
		else:
			store[char] += 1

	for char in S:
		if char in store:
			res += [char]*store[char]
			del store[char]

	for key in store:
		res += [key]*store[key]
	return ''.join(res)



S = "cbafg"
T = "abcd"
print customSortString(S, T)
