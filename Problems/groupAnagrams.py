

def groupAnagrams(strs):
	store = {}

	print ord('b')-ord('a')

	for s in strs:
		counts = [0] * 26
		for char in s:
			counts[ord(char)-ord('a')] += 1
		key = tuple(counts)
		if key not in store:
			store[key] = [s]
		else:
			store[key].append(s)

	return store.values()



strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print groupAnagrams(strs)
