def battleship(matrix):
	if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
		return 0
	count = 0
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 'X' and (i == 0 or matrix[i-1][j] != 'X') and (j == 0 or matrix[i][j-1] != 'X'):
				count += 1
	return count

print battleship([['X','.','.','X'],['.','.','.','X'],['.','.','.','X']])