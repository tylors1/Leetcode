def increasingTriplet(nums):
	low = mid = float('inf')

	for num in nums:
		if num < low:
			low = num
		if low < num < mid:
			mid = num
		if num > mid:
			return True
	return False



nums = [6,7,1,2]
# nums = [6,7,1,2,8]
print increasingTriplet(nums)