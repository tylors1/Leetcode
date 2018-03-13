def setZeroes(matrix):
	# for i in range(len(matrix)):
	# 	for j in range(len(matrix[0])):
	# 		if matrix[i][j] == 0:
	# 			for h in range(len(matrix)):
	# 				if matrix[h][j] != 0:
	# 					matrix[h][j] = 'x'
	# 			for h in range(len(matrix[0])):
	# 				if matrix[i][h] != 0:
	# 					matrix[i][h] = 'x'	
	# for i in range(len(matrix)):
	# 	for j in range(len(matrix[0])):
	# 		if matrix[i][j] == 'x':
	# 			matrix[i][j] = 0
	# return matrix
	col0 = 1
	for i in range(len(matrix)):
		if matrix[i][0] == 0:
			col0 = 0
		for j in range(len(matrix[0]))[1:]:
			if matrix[i][j] == 0:
				matrix[i][0] = 0
				matrix[0][j] = 0
	print matrix
	for i in range(len(matrix))[::-1]:
		for j in range(len(matrix[0]))[1::-1]:
			if matrix[i][0] == 0 or matrix[0][j] == 0:
				matrix[i][j] = 0
		if col0 == 0:
			matrix[i][0] == 0

	return matrix




# matrix = [[1, 1, 1, 1, 1],
# 		[1, 1, 0, 1, 1],
# 		[1, 1, 1, 0, 1],
# 		[1, 1, 1, 1, 1],
# 		[1, 1, 1, 1, 1]]

# matrix = [[0,0,0,5],
# 		[4,3,1,4],
# 		[0,1,1,4],
# 		[1,2,1,3],
# 		[0,0,1,1]]

matrix = [[1,1,1],
		[0,1,2]]
for row in setZeroes(matrix):
	print row