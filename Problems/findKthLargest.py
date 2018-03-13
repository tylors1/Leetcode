import heapq
def findKthLargest(nums, k):
	heap = []
	for num in nums:
		heapq.heappush(heap, num)
	for i in range(len(nums)-k):
		heapq.heappop(heap)
	return heapq.heappop(heap)


nums = [3,2,1,5,6,4]
k = 3

print findKthLargest(nums, k)