

def calPoints(ops):

	st = []
	curr = 0

	for op in ops:
		if op == "C":
			curr -= st.pop()
		elif op == "D":
			curr += st[-1]*2
			st.append(st[-1]*2)
		elif op == "+":
			curr += st[-1]+st[-2]
			st.append(st[-1]+st[-2])
		else:
			curr += int(op)
			st.append(int(op))
	return curr


ops = ["5","2","C","D","+"]
ops = ["5","-2","4","C","D","9","+","+"]
print calPoints(ops)