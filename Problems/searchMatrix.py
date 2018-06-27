

def searchMatrix(matrix, target):

	r = len(matrix[0])-1
	u = 0

	while r >= 0 and u < len(matrix):
		print matrix[u][r]
		if matrix[u][r] == target:
			return True
		elif matrix[u][r] > target:
			r -= 1
		else:
			u += 1
	return False



matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 0
print searchMatrix(matrix, target)



