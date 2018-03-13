def find_missing_int(nums):
	j = 0
	for i in range(len(nums)):
		if nums[i] > 0:
			nums[i], nums[j] = nums[j], nums[i]
			j += 1

	for i in range(0, j):
		if nums[abs(nums[i])-1] > 0:
			nums[abs(nums[i])-1] *= -1

	for i in range(0, j):
		if nums[i] > 0:
			return i+1
	return j+1



nums = [3, 4, -1, 1]
nums = [1, 2, 3]

print find_missing_int(nums)