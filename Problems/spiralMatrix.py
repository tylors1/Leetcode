

def print_matrix(matrix):
	row_top = 0
	col_left = 0
	row_bottom = len(matrix) - 1
	col_right = len(matrix[0]) - 1

	while True:

		while row_top <= row_bottom and col_left <= col_right:
			for i in range(col_left, col_right+1):
				print matrix[row_top][i]
			row_top += 1
			for i in range(row_top, row_bottom+1):
				print matrix[i][col_right]
			col_right -= 1
			for i in range(col_right+1, col_left, -1):
				print matrix[row_bottom][i]
			row_bottom -= 1
			for i in range(row_bottom+1, row_top, -1):
				print matrix[i][col_left]
			col_left += 1


		break


matrix = [[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]

print print_matrix(matrix)