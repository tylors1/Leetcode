def sortColors(nums):
	l = m = 0
	h = len(nums) - 1
	while m <= h:
		if nums[m] == 1:
			m += 1
		elif nums[m] == 2:
			nums[m], nums[h] = nums[h], nums[m]
			h -= 1
		elif nums[m] == 0:
			nums[m], nums[l] = nums[l], nums[m]
			m += 1
			l += 1
		print nums





nums = [1,2,0,0,1,2,0,2,1,2,1]
# nums = [1]
# nums = [0,2,1]

sortColors(nums)