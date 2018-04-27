# https://leetcode.com/problems/next-greater-element-i/description/


def next_greater(findNums, nums):
	store = {}
	res = []
	stack = []

	for num in nums:
		while len(stack) and stack[-1] < num:
			store[stack.pop()] = num 
		stack.append(num)
	for num in findNums:
		res.append(store.get(num, -1))


	return res


nums1 = [2,4]
nums2 = [1,2,3,4]
print next_greater(nums1, nums2)