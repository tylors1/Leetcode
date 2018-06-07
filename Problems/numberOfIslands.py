# Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring and their perimiter is surrounded by water.

# For example, this matrix has 4 islands.

# 1 0 0 0 0
# 0 0 1 1 0
# 0 1 1 0 0
# 0 0 0 0 0
# 1 1 0 0 1
# 1 1 0 0 1

def numOfIslands(matrix):

	count = 0
	
	def dfs(matrix, i, j):
		if i < 0 or j < 0 or i > len(matrix)-1 or j > len(matrix[0])-1 or matrix[i][j] == 0:
			return
		matrix[i][j] = 0
		dfs(matrix, i, j+1)
		dfs(matrix, i, j-1)
		dfs(matrix, i+1, j)
		dfs(matrix, i-1, j)

	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 1:
				dfs(matrix, i, j)
				count += 1



	return count





matrix = [[1, 0, 0, 0, 0],
[0, 0, 1, 1, 0],
[0, 1, 1, 0, 0],
[0, 0, 0, 0, 0],
[1, 1, 0, 0, 1],
[1, 1, 0, 0, 1]]

print numOfIslands(matrix)