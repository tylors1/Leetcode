# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

#     1, 1, 1, 1
#     2, 1, 1
#     1, 2, 1
#     1, 1, 2
#     2, 2


def climb_stairs(n):


	a, b = 0, 1
	for i in range(n+1):
		a, b = b, a+b
	return a

stairs = 5
print climb_stairs(stairs)