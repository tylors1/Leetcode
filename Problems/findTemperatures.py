def findTemperatures(temperatures):
	res = [0] * len(temperatures)
	stack = []

	for i in range(len(temperatures)):
		if stack:
			while stack and stack[-1][0] < temperatures[i]:
				n = stack.pop()[1]
				res[n] = i - n
		if i < len(temperatures)-1 and temperatures[i] < temperatures[i+1]:
			res[i] = 1
		else:
			stack.append([temperatures[i], i])
	return res






temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
temperatures = [77,77,77,77,77,41,77,41,41,77]
print findTemperatures(temperatures)