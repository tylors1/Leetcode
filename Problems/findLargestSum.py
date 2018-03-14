# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 8] should return 12, since we pick 4 and 8. [5, 1, 1, 5] should return 10, since we pick 5 and 5.




def findSum(nums):
	max1 = nums[0]
	maxi = 0
	for i in range(len(nums))[1:]:
		if max1 < nums[i]:
			max1 = nums[i]
			maxi = i
	




nums = [2,4,7,8,9]
print findSum(nums)