from bisect import bisect_left
def is_subsequence(s, t):

	if s == "":
		return True

	count = 0
	for c in t:
		if c == s[count]:
			count += 1
		if count == len(s):
			return True
	return False

def is_subsequence_dp(s, t):
	# create map with chars index locations
	store = {}
	for i in range(len(t)):
		if t[i] not in store:
			store[t[i]] = [i]
		else:
			store[t[i]].append(i)

	lowBound = 0

	for char in s:
		if char not in store:
			return False
		idx_list = store[char] # get list of indices for char

		i = bisect_left(idx_list, lowBound) # search list for index thats at least a low bound
		if i == len(idx_list):	# if index is at end of list, lower bound is greater than greatest index of char in string t
			return False
		lowBound = idx_list[i] + 1 # move lowerbound to index of found char + 1
	return True




s = "abc"
t = "ahbgdc"
s = "axc"
t = "ahbgdc"
print is_subsequence(s, t)

print is_subsequence_dp(s, t)