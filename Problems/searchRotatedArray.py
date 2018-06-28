def search(nums, target):

	if len(nums) == 0:
		return -1

	lo = 0
	hi = len(nums) - 1

	while lo < hi:
		mid = (lo + hi) / 2
		if nums[mid] > nums[hi]:
			lo = mid + 1
		else:
			hi = mid - 1
	
	pivot = lo
	lo = 0
	hi = len(nums) - 1

	while lo <= hi:
		mid = (lo + hi) / 2
		realmid = (mid + pivot)%len(nums)
		if nums[realmid] == target:
			return realmid
		if nums[realmid] < target:
			lo = mid + 1
		else:
			hi = mid - 1
	return -1 













# nums = [8, 9, 2, 3, 4, 5, 6]
# nums = [4, 5, 6, 7, 8, 9, 1]
nums = [4, 5, 6, 7, 0, 1, 2]
target = 5

print search(nums, target)