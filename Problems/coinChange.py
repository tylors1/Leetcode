def coin_change(coins, amount):
	dp = [0] + [amount+1]*amount

	for coin in coins:
		for i in range(len(dp)):
			pass
	
	


coins = [1, 2, 5]
amount = 11
print coin_change(coins, amount)