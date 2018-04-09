from bisect import bisect_left
def isSubsequence(s, t):

	store = {}
	for i in range(len(t)):
		if t[i] not in store:
			store[t[i]] = [i]
		else:
			store[t[i]].append(i)
	lower = 0
	for i in range(len(s)):
		if s[i] not in store:
			return False
		idx = store[s[i]]
		j = bisect_left(idx, lower)
		if j == len(idx):
			return False
		lower = idx[j] + 1
	return True

s = "abc"
t = "ahbgdc"

print isSubsequence(s, t)