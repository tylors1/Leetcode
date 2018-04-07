def max_sub_array(nums):

	res = curr = nums[0]

	for num in nums[1:]:
		curr = max(num, num + curr)
		res = max(curr, res)
	return res




nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [3, -8, 1, 1, 1, 1]
print max_sub_array(nums)



# iterate each num
# calc if sum > next num

# for loop
# 	curr = max(curr, num)
# 	res = max(curr, res)