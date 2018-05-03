# An sorted array of integers was rotated an unknown number of times.

# Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

# For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

# nums = [4,5,6,7,0,1,2], target = 0, Output: 4

# nums = [2,4,5,6,7,0,1], target = 0, Output: 5

# nums = [10,0,1,2,3,4,5], target = 0, Output: 1

# if nums low <= nums mid
# 	if target between low and mid
# 		high = mid - 1
# 	else
# 		low = mid + 1
# else
# 	if target between mid and high
# 		low = mid + 1
# 	else
# 		high = mid - 1


def find_index(nums, target):

	low, high = 0, len(nums) - 1

	while low <= high:
		mid = (high + low)/2
		if nums[mid] == target:
			return mid
		elif nums[low] <= nums[mid]:
			if nums[low] <= target <= nums[mid]:
				high = mid - 1
			else:
				low = mid + 1
		else:
			if nums[mid] <= target <= nums[high]:
				low = mid + 1
			else:
				high = mid - 1
	return -1

nums = [13, 18, 25, 2, 8, 10] 
target = 8
print find_index(nums, target)




