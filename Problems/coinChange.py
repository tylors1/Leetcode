def coin_change(coins, amount):
	dp = [0] + [amount + 1 for i in range(amount)]
	
	for i in range(len(coins)):
		for j in range(coins[i], len(dp)):
			dp[j] = min(dp[j], dp[j-coins[i]] + 1)

	if dp[-1] > amount:
		return -1
	return dp[-1]


coins = [1,2,5]
coins = [2]
amount = 3
print coin_change(coins, amount)
