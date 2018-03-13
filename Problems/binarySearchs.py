def search(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: int
	"""
	
	l = 0
	r = len(nums) - 1
	while l <= r:

		mid = (l + r)//2;
		print l, mid, r

		if nums[mid] == target:
			return mid

		elif nums[mid] < target:
			l = mid + 1

		else:
			r = mid - 1
	return -1

nums = [-1,0,3,5,9,12]
target = 5
print search(nums, target)


