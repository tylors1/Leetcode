# get diffs and store in array
# if diffs arr < 2, return 1
# iterate diffs array
# 	if prod between each item is < 0, add +1 to wiggle len
# 	return wigg len + 1


def wiggle_length(nums):

	if len(nums) < 2:
		return len(nums)

	diffs = []
	for i in range(1, len(nums)):
		diff = nums[i]-nums[i-1]
		if diff != 0:
			diffs.append(diff)

	if len(diffs) == 0:
		return 1

	count = 1
	for i in range(1, len(diffs)):
		prod = diffs[i] * diffs[i-1]
		if prod < 0:
			count += 1
	return count + 1




nums = [1,2,3,4,5,6,7,8,9]
nums = [0,0]

print wiggle_length(nums)




