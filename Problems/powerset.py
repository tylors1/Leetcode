# The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

# For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

# You may also use a list or array to represent a set.

# iterate through items in arr
# 	start new subarray
# 	iterate through what added to res so far
# 		[add what is in res to new subarray, plus num iterating on in arr]
# 	add sub to res


def powerset(arr):
	res = [[]]
	for num in arr:
		sub = []
		print "res", res
		for item in res:
			print item, [num]
			sub += [item+[num]]
		res += sub

	return res

def powerset_no_dupes(arr):
	res = [[]]
	arr.sort()
	for i in range(len(arr)):
		if i == 0 or arr[i] != arr[i-1]:
			n = len(res)
			for j in range(len(res) - n, len(res)):
				res.append(res[j] + [arr[i]])
	return res


arr = [1, 3, 2]
print powerset(arr)


arr = [1, 3, 2, 2]
print powerset_no_dupes(arr)