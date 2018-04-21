# Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

# For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.




def max_profit(arr):

	curr = 0
	curr_min = arr[0]

	for num in arr[1:]:
		if num < curr_min:
			curr_min = num
		curr = max(num - curr_min, curr)
	return curr

arr = [9, 11, 8, 5, 7, 10]
print max_profit(arr)