# Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

# Integers can appear more than once in the list. You may assume all numbers in the list are positive.

# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24


def find_subset(arr, k):
	res = [set() for i in range(k+1)]
	arr.sort()
	res[0].add(())
	
	for num in arr:
		for i in range(k, num-1, -1):
			for prev in res[i-num]:
				res[i].add(prev +(num,))
		print res
	return list(res[-1])

# def find_subset2(arr, k):
# 	res = [[True]+[False]*k]*(len(arr)+1)

# 	for i in range(1, len(arr)):
# 		for j in range(1, k):
# 			if j-arr[i-1] >= 0:
# 				print i-1, j, res[i-1][j]
# 				res[i][j] = res[i-1][j] if not None else res[i-1][j-arr[i-1]]
# 			else:
# 				res[i][j] = res[i-1][j]
# 	print res
# 	return res[len(arr)][k]

k = 24
arr = [12, 1, 61, 5, 9, 2]
print find_subset(arr, k)
# print find_subset2(arr, k)
