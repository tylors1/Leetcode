def rob(nums):

	last, now = 0, 0

	for i in nums: 
		print i, last, now
		last, now = now, max(last + i, now)

	
	return now

print rob([30,50,30])