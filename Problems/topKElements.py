import heapq

def topKElements(nums, k):
	counts = {}

	for num in nums:
		if num not in counts:
			counts[num] = 1
		else:
			counts[num] += 1
	print counts

	return heapq.nlargest(k, counts, key=counts.get)

nums = [1,1,1,2,2,3]
k = 2
print topKElements(nums, k)