def minClimbStairs(cost):
	n = len(cost)
	dp = [0]*n
	dp[0] = cost[0]
	dp[1] = cost[1]

	for i in range(n)[2:]:
		dp[i] = cost[i] + min(dp[i-1], dp[i-2])
	return min(dp[n-1], dp[n-2])

# cost = [0,2,2,1]
# cost = [0,0,0,1]
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print minClimbStairs(cost)
