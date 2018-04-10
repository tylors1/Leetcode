def maxProfit(prices):
	curr_min = prices[0]
	curr_max = 0
	for price in prices[1:]:
		if price < curr_min:
			curr_min = price
		if price - curr_min > curr_max:
			curr_max = price - curr_min
	return curr_max


prices = [7, 1, 5, 3, 6, 4]
prices = [7, 6, 4, 3, 1]
print maxProfit(prices)