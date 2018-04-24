# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

# Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

# Do this in O(N) time.



def max_sum(arr):
	res = 0
	curr = 0

	for num in arr:
		curr = max(curr + num, 0)
		res = max(curr, res)
	return res



arr = [34, -50, 42, 14, -5, 86]
arr = [-5, -1, -8, -9]
arr = [-2,1,-3,4,-1,2,1,-5,4]
print max_sum(arr)



