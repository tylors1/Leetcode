# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

def edit_distance(a, b):

	matrix = [[0 for i in range(len(b)+1)] for j in range(len(a)+1)]

	for i in range(len(matrix[0])):
		matrix[0][i] = i

	for i in range(len(matrix)):
		matrix[i][0] = i

	for i in range(1, len(a)+1):
		for j in range(1, len(b)+1):
			if a[i-1] == b[j-1]:
				matrix[i][j] = matrix[i-1][j-1]
			else:
				matrix[i][j] = 1 + min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])

	return matrix[len(a)][len(b)]
	

		

def print_matrix(matrix):
	for row in matrix:
		print row

# word1 = "abcdef"
# word2 = "azced"

word1 = "intention"
word2 = "execution"

print edit_distance(word1, word2)