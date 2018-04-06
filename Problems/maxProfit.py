def max_profit(prices):
	curr = prices[0]
	res = 0
	for price in prices[1:]:
		if price < curr:
			curr = price
		if price - curr > res:
			res = price - curr
	return res


prices = [7, 1, 5, 3, 6, 4]
# prices = [7, 6, 4, 3, 1]
print max_profit(prices)