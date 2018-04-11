from bisect import bisect_left
def is_subsequence(s, t):
	store = {}

	for i in range(len(t)):
		if t[i] not in store:
			store[t[i]] = [i]
		else:
			store[t[i]].append(i)

	lower = 0
	for c in s:
		if c not in store:
			return False
		idx = bisect_left(store[c], lower)
		if idx == len(store[c]):
			return False
		lower = store[c][idx] + 1
	return True


s = "abcd"
t = "ahbgdc"

print is_subsequence(s, t)




