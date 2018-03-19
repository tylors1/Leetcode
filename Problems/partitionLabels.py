import collections
def partitionLabels(S):
	# set array to record last index of each element
	# iterate 2nd time 
	# 	sent end = to max of each char as iterate through
	# 	if i == end, add end - start to result array

	last = [0] * 26

	for i in range(len(S)):
		last[ord(S[i])-ord('a')] = i

	start = -1
	end = -1
	res = []
	for i in range(len(S)):
		if start == -1:
			start = i
		end = max(end, last[ord(S[i])-ord('a')])
		if end == i:
			res.append(end+1 - start)
			start = -1
	return res





S = "ababcbacadefegdehijhklij"
print partitionLabels(S)


# Below will return actual substrings ==============================================

# def partitionLabels(S):
# 	# iterate once, place 1st appearance and last of each char in map
# 	# iterate keys until value of next 1st appearacne of a char is higher than latest found max index
# 	if len(S) < 2:
# 		return [S]

# 	store = collections.OrderedDict()
# 	for i in range(len(S)):
# 		if S[i] not in store:
# 			store[S[i]] = [i, i]
# 		else:
# 			store[S[i]][1] = i
# 	res = []
# 	prev = max_found = count = 0
# 	for key in store:
# 		if count == 0:
# 			max_found = store[key][1]
# 			count += 1
# 		else:
# 			if store[key][0] > max_found:
# 				res.append(S[prev:max_found+1])
# 				prev = max_found + 1
# 				max_found = store[key][1]
# 			if store[key][1] > max_found:
# 				max_found = store[key][1]
# 	if max_found - prev > 0:
# 		res.append(S[prev:max_found+1])
# 	return res