

def wiggle_max_len(nums):
	

	if len(nums) < 2:
		return len(nums)

	# create array of differences
	# if len is 0, return 1

	# count = 1
	# iterate differences array, find product between each item
	# if negative, add 1 to count

	diffs = []
	for i in range(1, len(nums)):
		item = nums[i] - nums[i-1]
		if item != 0:
			diffs.append(item)

	if len(diffs) == 0:
		return 1

	res = 1
	for i in range(1, len(diffs)):
		prod = diffs[i] * diffs[i-1]
		if prod < 0:
			res += 1
	return res + 1







# nums = [3,3,3,2,5]
nums = [1,17,5,10,13,15,10,5,16,8]
# nums = [0,0]
print wiggle_max_len(nums)