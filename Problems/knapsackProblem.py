def knapsack(W, wt, val):
	table = [[0 for i in range(W+1)] for j in range(len(val)+1)]

	for i in range(len(val)+1):
		for j in range(W+1):
			if i == 0 or j == 0:
				table[i][j] = 0
			elif wt[i-1] <= j:
				table[i][j] = max(val[i-1] + table[i-1][j-wt[i-1]], table[i-1][j])
			else:
				table[i][j] = table[i-1][j]



	print table

	return table[len(val)][W]







# val = [60, 100, 120]
# wt = [10, 20, 30]
# W = 50
# n = len(val)

val = [1, 4, 5, 7]
wt = [1, 3, 4, 5]
W = 7


print knapsack(W, wt, val)