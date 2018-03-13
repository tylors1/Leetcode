def climb_stairs(n, jumps):


	steps = [0] * (n+1)
	steps[0] = 1

	for j in range(len(jumps)):
		for step in range(jumps[j], len(steps)):
			step_sum = 0
			for k in range(j+1):
				step_sum += steps[step-jumps[k]]
				print k, steps
			steps[step] = step_sum
	return steps[n]



print climb_stairs(10, [2, 3, 5])