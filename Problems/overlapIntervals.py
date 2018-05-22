# Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

# The input list is not necessarily ordered in any way.

# For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].


def overlaps(nums):
	res = [nums[0]]
	nums = sorted(nums, key=lambda x: x[0])
	print nums
	for i in range(1, len(nums)):
		if res[-1][1] >= nums[i][0]:
			res[-1][1] = max(nums[i][1], res[-1][1])
		else:
			res.append(nums[i])

	return res

nums = [[1, 3], [5, 8], [4, 10], [20, 25]]
# nums = [[1,3],[2,6],[8,10],[15,18]]
# nums = [[1,4],[4,5]]
print overlaps(nums)
