def productExceptSelf(nums):
	res = []
	p = 1
	for i in range(len(nums)):
		res.append(p)
		p = p * nums[i]

	p = 1
	for i in range(len(nums))[-1::-1]:
		res[i] *= p
		p *= nums[i]

	return res
nums = [1, 2, 3, 4, 5]
nums = [3, 2, 1]
print productExceptSelf(nums)