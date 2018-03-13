def validParenthesis(s):

	st = []

	for char in s:
		if char == '[' or char == '(' or char == '{':
			st.append(char)
		elif char == '}':
			if st.pop() != '{':
				return False
		elif char == ')':
			if st.pop() != '(':
				return False
		elif char == ']':
			if st.pop() != '[':
				return False
	if len(st) == 0:				
		return True
	else:
		return False

s = "()[]{}"
s= "([)]"

print validParenthesis(s)