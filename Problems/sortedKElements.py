from heapq import heappush, heappop
def sortArray(a, k):
	
	window_width = k + 1
	window_heap = []
	result_array = []
	index = 0

	for i in range(window_width):
		heappush(window_heap, a[i])

	while index + window_width < len(a):
		result_array.append(heappop(window_heap))
		heappush(window_heap, a[window_width + index])
		index += 1

	while window_heap:
		result_array.append(heappop(window_heap))

	return result_array


arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
k = 2
print sortArray(arr, k)