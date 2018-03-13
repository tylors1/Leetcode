def canJump(nums):
	count = nums[0]

	for i in range(len(nums)):
		if i == len(nums)-1:
			return True
		print count, nums[i]
		if count <= 0 and nums[i] == 0:
			return False
		if nums[i] >= count:
			count = nums[i]
		count -= 1
	return True



nums = [3,2,1,0,4]
# nums = [0,1]
# nums = [2,3,1,1,4]
print canJump(nums)

