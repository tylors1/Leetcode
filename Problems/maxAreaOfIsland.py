def maxAreaOfIsland(grid):

	def dfs(i, j, grid):
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
			return
		count[0] += 1
		grid[i][j] = 0
		dfs(i+1, j, grid)
		dfs(i-1, j, grid)
		dfs(i, j+1, grid)
		dfs(i, j-1, grid)


	max_count = 0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 1:
				count = [0]
				dfs(i, j, grid)				
				max_count = max(count[0], max_count)
	return max_count



grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print maxAreaOfIsland(grid)