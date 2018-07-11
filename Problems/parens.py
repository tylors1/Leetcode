

def is_balanced(parens):
	store = {')':'(', '}':'{', ']':'['}
	if len(parens) % 2 != 0:
		return False
	stack = []
	for i in range(len(parens)):
		if parens[i] in store.values():
			stack.append(parens[i])
		elif parens[i] in store:
			if len(stack) == 0 or store[parens[i]] != stack.pop():
				return False
		else:
			return False
	return stack == []


parens = "()"
print is_balanced(parens)






