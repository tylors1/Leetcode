# https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/

def skyline(grid):
# get max of each row/col
# each item of res is min of the max row/col

	res = 0
	cols = []
	rows = []
	for col in zip(*grid):
		cols.append(max(col))
	for row in grid:
		rows.append(max(row))
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			# grid[i][j] = min(cols[j], rows[i]) - comment line 17 and uncomment this line to return new grid
			res += min(cols[j], rows[i]) - grid[i][j]
	return res


grid = [ [3, 0, 8, 4], 
  		[2, 4, 5, 7],
  		[9, 2, 6, 3],
  		[0, 3, 1, 0] ]

print skyline(grid)
