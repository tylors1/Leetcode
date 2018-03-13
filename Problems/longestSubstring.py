def longestSubstring(s, k):
	if k == 0 or s == None or len(s) == 0:
		return 0

	if len(s) < k:
		return s

	store = {}

	max_len = k
	left = 0
	right = 0
	for i in range(len(s)):
		if s[i] in store:
			store[s[i]] += 1
		else:
			store[s[i]] = 1
		print store
		if len(store) > k:
			max_len = max(max_len, i-left)
			while len(store) > k:
				if store[s[left]] == 1:
					store.pop(s[left])
				else:
					store[s[left]] -= 1
				left += 1
			right = i

	return s[left:right]


s = "abcadcacacaca" 
k = 3

print longestSubstring(s, k)