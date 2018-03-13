def groupAnagrams(strs):
	store = {}
	for s in strs:
		temp = ''.join(sorted(s))
		if temp not in store:
			store[temp] = [s]
		else:
			store[temp].append(s)
	return list(store.values())
			


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print groupAnagrams(strs)
