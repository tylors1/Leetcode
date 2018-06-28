

def searchMatrix(matrix, target):
	if matrix == []:
		return False

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

def searchMatrix2(matrix, target):
	if matrix == []:
		return False

	r, c = len(matrix), len(matrix[0])
	l, h = 0, r * c - 1

	while l <= h:
		mid = (l + h) / 2
		num = matrix[mid/c][mid%c]

		print mid, c
		print mid/c, mid%c

		if num == target:
			return True
		elif num < target:
			l = mid + 1
		else:
			h = mid - 1
	return False


matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 23
print searchMatrix2(matrix, target)



