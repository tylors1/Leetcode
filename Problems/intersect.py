def intersect(nums1, nums2):
	store = {}
	res = []
	if len(nums1) >= len(nums2):
		big, small = nums1, nums2
	else:
		big, small = nums2, nums1
	for num in big:
		if num not in store:
			store[num] = 1
		else:
			store[num] += 1
	for num in small:
		if num in store and store[num] > 0:
			store[num] -= 1
			res.append(num)
	return res






nums1 = [1, 2, 2, 1]
nums2 = [2,2]

print intersect(nums1, nums2)