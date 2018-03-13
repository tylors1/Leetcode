def island_perimeter(matrix):
	count = 0
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 1:
				count += 4
				if i > 0 and matrix[i-1][j] == 1:
					count -= 2
				if j > 0 and matrix[i][j-1] == 1:
					count -= 2
	return count





print island_perimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])