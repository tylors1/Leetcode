def move_zeroes(nums):
	i = 0
	j = 0
	while i < len(nums) and j < len(nums):
		print i, nums[i], nums
		if nums[i] == 0:
			nums.append(nums.pop(i))
		else:
			i += 1
		j += 1
	return nums

print move_zeroes([0,0,1])