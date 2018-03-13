def findSum(nums, k):
	nums = sorted(nums)
	print nums
	l = 0
	r = len(nums) - 1

	while l < r:
		n = nums[l] + nums[r]
		if n == k:
			print nums[l], nums[r]
			return True
		if n > k:
			r -= 1
		else:
			l += 1
	return False





nums = [1, 4, 2, 7, 9, 10]
k = 15
print findSum(nums, k)