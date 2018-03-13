def rotate(matrix):
	n = len(matrix)
	for i in range(n):
		for j in range(i, len(matrix[0])):
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
	print matrix
	for i in range(n):
		for j in range(len(matrix[0])/2):
			matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

print rotate(matrix)