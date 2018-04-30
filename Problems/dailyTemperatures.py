


def dailyTemperatures(temperatures):

	res = [0] * len(temperatures)
	stack = []

	for i in range(0, len(temperatures)):
		while stack and stack[-1][0] < temperatures[i]:
			temp = stack.pop()
			res[temp[1]] = i - temp[1]
		if i != len(temperatures)-1 and temperatures[i+1] > temperatures[i]:
			res[i] = 1
		else:
			stack.append([temperatures[i],i])
	return res









temperatures = [77,77,77,77,77,41,77,41,41,77]
print dailyTemperatures(temperatures)