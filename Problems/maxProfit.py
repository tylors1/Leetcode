# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

def maxProfit(prices):
    if len(prices) == 0:
        return 0
    
    low = prices[0]
    res = 0
    for num in prices:
        if low > num:
            low = num
        if num - low > res:
            res = num - low
    return res 

prices = [7, 1, 5, 3, 6, 4]
print maxProfit(prices)