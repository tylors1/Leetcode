
# keeping track of:
# total sum
# two pointers/values:
# 	valid play 1
# 	valid play 2


def calPoints(ops):

	total = 0
	stack = []

	for i in range(len(ops)):
		print stack
		if ops[i] == "+":
			stack.append(stack[-1] + stack[-2])
			total += stack[-1]
			# print "add ", stack[-1]
		elif ops[i] == "C":
			# print "subtract ", stack[-1]
			total -= stack.pop()
		elif ops[i] == "D":
			stack.append(stack[-1] * 2)
			# print "add ", stack[-1]
			total += stack[-1]
		else:
			stack.append(int(ops[i]))
			total += stack[-1]
	return total







# lol = ["5","2","C","D","+"]
lol = ["5","-2","4","C","D","9","+","+"]
print calPoints(lol)