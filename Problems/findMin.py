
# [10,0,1,2,3,4,5,6]
# [3,4,5,6,8,10]

def findMin(nums):
	if not nums:
		return []

	low, high = 0, len(nums) - 1
	while low < high:
		mid = (low+high)/2
		if nums[low] < nums[high]:
			return nums[low]
		elif mid > 0 and nums[mid-1] > nums[mid]:
			return nums[mid]
		elif nums[mid] >= nums[low]:
			low = mid + 1
		else:
			high = mid - 1

	return nums[low]


nums = [3,4,5,1,2] 
print findMin(nums)



