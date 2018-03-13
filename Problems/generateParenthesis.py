def generateParenthesis(n):
	def helper(res, curr, parens, parens_left, n):
		if len(curr) == n*2:
			res.append(curr)
			return
		if parens > parens_left:
			helper(res, curr + ')', parens, parens_left + 1, n)
		if parens < n:
			helper(res, curr + '(', parens + 1, parens_left, n)

	res = []
	helper(res, "", 0, 0, n)
	return res





n = 3
print generateParenthesis(n)