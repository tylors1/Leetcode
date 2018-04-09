

def numSquares(n):
	dp = [n] * (n+1)
	dp[0] = 0
	for i in range(1, n+1):
		mini = float('inf')
		j = 1
		while i - j*j >= 0:
			mini = min(mini, dp[i-(j*j)] + 1)
			print dp, i - j*j
			j += 1
		dp[i] = mini
	return dp[n]


n = 15
print numSquares(n)


