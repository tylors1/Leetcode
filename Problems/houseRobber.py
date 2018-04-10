def rob(nums):
	a = nums[0]
	b = 0
	for num in nums[1:]:
		a, b = max(a, b + num), a
	return a


nums = [5, 4, 5, 6, 9]
print rob(nums)