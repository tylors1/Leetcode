
def max_subarray(nums):
	res = nums[0]
	last = res
	for i in range(1, len(nums)):
		curr = max(last + nums[i], nums[i]) # curr is max of number iterating at vs. prev element + number iterating at
		res = max(res, curr) # res max of largest sum found or curr sum
		last = curr # save curr found sum for next iteration
		print curr
	return res



nums = [-2,1,-3,4,-1,2,1,-5,4]
print max_subarray(nums)