def judge_circle(moves):
	x = 0
	y = 0
	for move in moves:
		if move == 'U':
			y += 1
		elif move == 'D':
			y -= 1
		elif move == 'L':
			x -= 1
		else:
			x += 1
	if x == 0 and y == 0:
		return True
	else:
		return False

print judge_circle("UD")