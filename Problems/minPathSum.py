# get sums on top row and 1st column
# nested fors
# 	find min sum at each item, sum being current + top or from left

def min_path_sum(grid):
	n = len(grid)
	m = len(grid[0])

	for i in range(1, n):
		grid[i][0] = grid[i][0] + grid[i-1][0]

	for i in range(1, m):
		grid[0][i] = grid[0][i] + grid[0][i-1]

	for i in range(1,n):
		for j in range(1,m):
			grid[i][j] = min(grid[i][j] + grid[i][j-1], grid[i][j] + grid[i-1][j])

	return grid[n-1][m-1]

grid = [[1,3,1],[1,5,1],[4,2,1]]

print min_path_sum(grid)