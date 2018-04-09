

def numSquares(n):
	dp = [n] * (n+1)
	dp[0] = 0
	for i in range(1, n+1):
		mini = float('inf')
		j = 1
		print i, j*j, i - j*j
		while i - j*j >= 0:
			mini = min(mini, dp[i-(j*j)] + 1)
			j += 1
		dp[i] = mini
	print dp
	return dp[n]




n = 15
print numSquares(n)


