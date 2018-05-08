# # Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

# For example, given the following matrix:

# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
# # and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.

def find_word(matrix, target):
	# check top rows
	for i in range(0, len(matrix)-len(target)+1):
		for j in range(0, len(matrix[0])):
			if matrix[i][j] == target[0]:
				for k in range(1, len(target)):
					if matrix[i+k][j] != target[k]:
						break
					elif k == len(target)-1:
						return True

	# check bottom left
	for i in range(len(matrix)-len(target)+1, len(matrix)):
		for j in range(0, len(matrix[0])-len(target)+1):
			if matrix[i][j] == target[0]:
				print matrix[i][j], target[0]
				for k in range(1, len(target)):
					print matrix[i][j+k], target[k], k, len(target)
					if matrix[i][j+k] != target[k]:
						break
					elif k == len(target)-1:
						return True
	return False




target = "MASS"
matrix = [['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

print find_word(matrix, target)