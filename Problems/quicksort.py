

def quicksort(nums):

	less = []
	equal = []
	greater = []

	if len(nums) > 1:
		pivot = nums[0]
		for num in nums:
			if num < pivot:
				less.append(num)
			if num ==  pivot:
				equal.append(num)
			if num > pivot:
				greater.append(num)
		return quicksort(less)+equal+quicksort(greater)
	else:
		return nums

def partition(nums, begin, end):
	pivot = begin
	print
	print
	for i in range(begin+1, end+1):
		print nums[i], nums[begin]
		if nums[i] <= nums[begin]:
			pivot += 1
			nums[i], nums[pivot] = nums[pivot], nums[i]
	nums[pivot], nums[begin] = nums[begin], nums[pivot]
	return pivot


def quicksort2(nums, begin=0, end=None):
	if end is None:
		end = len(nums)-1
	def helper(nums, begin, end):
		if begin >= end:
			return
		pivot = partition(nums, begin, end)
		helper(nums, begin, pivot-1)
		helper(nums, pivot+1, end)
	return helper(nums, begin, end)


nums = [5,3,2,10,9,4]
quicksort2(nums)
print nums