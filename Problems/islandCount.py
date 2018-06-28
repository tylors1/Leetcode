

def countIslands(matrix):
	count = 0

	def dfs(matrix, i, j):
		if i < 0 or i > len(matrix)-1 or j < 0 or j > len(matrix[0])-1 or matrix[i][j] == 0:
			return
		matrix[i][j] = 0
		dfs(matrix, i+1, j)
		dfs(matrix, i, j+1)
		dfs(matrix, i-1, j)
		dfs(matrix, i, j-1)


	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 1:
				dfs(matrix, i, j)
				count += 1

	return count


matrix = [ [0,    1,    0,    1,    0],
		[0,    0,    1,    1,    1],
		[1,    0,    0,    1,    0],
		[0,    1,    1,    0,    0],
		[1,    0,    1,    0,    1] ]
print countIslands(matrix)
