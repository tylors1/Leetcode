def lengthOfLIS(nums):

	def binary_search(nums, t, end, s):
		start = 0
		mid = 0
		l = end

		while(start <= end):
			mid = (start + end)/2
			if mid < l and nums[t[mid]] < s and s <= nums[t[mid + 1]]:
				return mid + 1
			elif nums[t[mid]] < s:
				start = mid + 1
			else:
				end = mid - 1
		return -1


	length = 0
	r = [-1] * len(nums)
	t = [None] * len(nums)
	t[0] = nums[0]
	for i in range(1, len(nums)):
		if nums[t[0]] > nums[i]:
			t[0] = i
		elif nums[i] > nums[t[length]]:
			length += 1
			t[length] = i
		else:
			index = binary_search(nums, t, length, nums[i])
			t[index] = i
			r[t[index]] = t[index-1]

	index = t[length]
	while index != -1:
		print nums[index],
		index = r[index]

	return length+1






# nums = [10, 9, 2, 5, 3, 7, 101, 18]
nums = [3, 4, -1, 5, 8, 2, 3, 12, 7, 9, 10]

print lengthOfLIS(nums)
