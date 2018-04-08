from bisect import bisect_left
def is_subsequence(s, t):

	# store index list for each char in map for t
	# iterate s, get next index of each char with binary search

	store = {}

	for i in range(len(t)):
		if t[i] not in store:
			store[t[i]] = [i]
		else:
			store[t[i]].append(i)

	lowerbound = 0
	for i in range(len(s)):
		if s[i] not in store:
			return False
		idx = store[s[i]]
		j = bisect_left(idx, lowerbound)
		if j == len(idx):
			return False
		lowerbound = idx[j] + 1
	return True




s = "abc"
t = "ahbgdc"

s = "axc"
t = "ahbgdc"
print is_subsequence(s, t)