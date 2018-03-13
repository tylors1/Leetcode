def findSubSets(arr, total):
	return rec(arr, total, len(arr) - 1)

	def rec(arr, total, i):
		if total == 0:
			return 1
		else if total < 0:
			return 0
		else if i < 0:
			return 0
		else if total < arr[i]:
			return rec(arr, total, i-1)
		else:
			return rec(arr, total - arr[i], i-1) + rec(arr, total, i-1)






arr = [2, 4, 6, 10]

print findSubSets(arr, 16)