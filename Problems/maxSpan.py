# http://codingbat.com/prob/p189576



def max_span(nums):
	store = {}
	res = 0

	for i in range(len(nums)):
		if nums[i] not in store:
			store[nums[i]] = i
		else:
			res = max(res, i - store[nums[i]])
	return res + 1








nums = [1, 2, 1, 1, 3]
nums = [1, 4, 2, 1, 4, 1, 4]
print max_span(nums)