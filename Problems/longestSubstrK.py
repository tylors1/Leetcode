# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

# iterate through 1 to len of s
# 	if char not in store, store with vale 1
# 	else += 1
# 	end += 1
# 	if number of uniqua chars are more than k, start forward
# 	if end - start + 1 is greater than largest found window size so far, save window size and start
# return s[window start: window start + window size]


def getSubstring(s, k):

	def less_than_k(store, k):
		count = 0
		for key in store:
			if store[key] > 0:
				count += 1
		return count <= k


	start = 0
	end = 0
	window_size = 1
	window_start = 0
	store = {}
	store[s[0]] = 1

	for i in range(1, len(s)):
		char = s[i]
		if char not in store:
			store[char] = 1
		else:
			store[char] += 1
		end += 1

		while not less_than_k(store, k):
			store[s[start]] -= 1
			start += 1
		if end - start + 1 > window_size:
			window_size = end - start + 1
			window_start = start
	return s[window_start:window_start+window_size]



s = "abcba"
k = 2

print getSubstring(s, k)