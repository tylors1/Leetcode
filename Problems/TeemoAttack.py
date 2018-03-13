def find_duration(timeSeries, duration):
	total = 0
	if timeSeries == None:
		return 0
	if len
	for i in range(len(timeSeries))[:-1]:
		print timeSeries[i+1] - timeSeries[i], duration
		if timeSeries[i+1] - timeSeries[i] > duration:
			total += duration
		else:
			total += timeSeries[i+1]-timeSeries[i]
	return total + duration





print find_duration([1,2,3,4,5,6,7,8,9], 2)