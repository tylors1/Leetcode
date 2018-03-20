# https://leetcode.com/problems/toeplitz-matrix/description/


# [0,0] [0,1] [0,2] [0,3]
# [1,0] [1,1] [1,2] [1,3]
# [2,0] [2,1] [2,2] [2,3]

def isToeplitzMatrix(matrix):
	row = len(matrix)-1
	col = 0

	for i in range(len(matrix)-1):
		for j in range(len(matrix[0])-1):
			print matrix[i][j], i, j
			if matrix[i][j] != matrix[i+1][j+1]:
				return False
	return True



matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]

print isToeplitzMatrix(matrix)


