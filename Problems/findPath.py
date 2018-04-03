# You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

# Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

# For example, given the following board:

# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]

# and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.


# get false neighbors from start
# while stack
# 	take closest neighbor(closest in distance to end)
# 	add curr to visited set
# 	add all neighbors to stack, sorted by distance to end
# 	continue until reach end, or stack no longer exists(no solution)

from heapq import heappop, heappush

def heuristic(curr, end):
	return abs(curr[0]-end[0]) + abs(curr[1]-end[1])

def findPath(matrix, start, end):
	q = []
	heappush(q, (0 + heuristic(start, end), 0, "", start))
	visited = set()
	
	print q
	

	











matrix = [[False, False, False, False],
[True, True, False, True],
[False, False, False, False],
[False, False, False, False]]
start = [3,0]
end = [0,0]

print findPath(matrix, start, end)