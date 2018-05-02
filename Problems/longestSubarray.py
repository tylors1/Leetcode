# subarray sum  - find the longest subarray sequence 
   #                 that adds up to a target 


# FOLLOW UPS: 
# 1. How would we modify this if we're looking for min subarray sequence? 
# 2. How would we modify this if we're looking for min subarray sequence equal to OR greater than target?


def longestSubarray(nums, k):
	curr = 0
	l = r = 0
	res = 0
	while r < len(nums):
		while r < len(nums) and curr < k:
			curr += nums[r]
			r += 1
		while l < r and curr > k:
			curr -= nums[l]
			l += 1
		if curr == k:
			res = max(res, r-l)
			curr -= nums[l]
			l += 1
	return res

k = 10
# nums = [1,1,1,1,1,1,1,1,1,1,5,5]
nums = [1,1,1,1,1,5]
print longestSubarray(nums, 10)
