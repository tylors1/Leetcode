

# Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

# For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

# Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array


def decreasing(nums):
	count = 0

	for i in range(len(nums)-1):
		if nums[i] == nums[i+1]:
			if i+1 == len(nums):
				return True
			elif i < len(nums)-2 and nums[i+2] - nums[i+1] == 1:
				return False
			else:
				count += 1
		if nums[i] > nums[i+1]:
			count += 1
		if count > 1:
			return False 
	return True

# nums = [10, 5, 7]
# nums = [10, 5, 1]
nums = [3, 5, 6, 6, 7]
print decreasing(nums)
