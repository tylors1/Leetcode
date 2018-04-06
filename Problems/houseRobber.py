def robber(houses):

	last = now = 0
	for house in houses:
		last, now = now, max(last + house, now)

	return now

houses = [4, 1, 5, 6, 7, 2, 5]
print robber(houses)