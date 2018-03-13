import heapq
def kthSmallest(matrix, k):

	flat = [x for sublist in matrix for x in sublist]
	

	heapq.heapify(flat)
	return heapq.nsmallest(k, flat)[-1]






k = 8
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]

print kthSmallest(matrix, k)