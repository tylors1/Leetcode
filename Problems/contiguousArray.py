# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1. 


def findMaxLength(nums):

	count = 0
	res = 0
	store = {0:0}

	for i, num in enumerate(nums,1):
		if num == 1:
			count += 1		
		else:
			count -= 1
		if count not in store:
			store[count] = i
		else:
			if i - store[count] > res:
				res = i - store[count]
	return res





nums = [0, 1]

print findMaxLength(nums)