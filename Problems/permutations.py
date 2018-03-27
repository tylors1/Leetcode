



def permute(s):

	chars = list(s)
	res = []

	def recurse(s, i):
		if i == len(s):
			res.append(''.join(s))
			return
		for j in range(i, len(s)):
			s[j], s[i] = s[i], s[j]
			recurse(s, i+1)
			s[j], s[i] = s[i], s[j]
			

		return res
	return recurse(chars, 0)




s = "abc"
print permute(s)