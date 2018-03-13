def searchMatrix(matrix, target):
	if matrix == None or len(matrix) < 1 or len(matrix[0]) < 1:
		return False

	c = len(matrix[0]) - 1
	r = 0
	while r < len(matrix) and c >= 0:
		if matrix[r][c] == target:
			return True
		elif matrix[r][c] > target:
			c -= 1
		else:
			r += 1
	return False





# matrix = [[1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]]
# target = 18

matrix = [[-1],[-1]]
target = -2

print searchMatrix(matrix, target)