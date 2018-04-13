# http://codingbat.com/prob/p117334



def string_splosion(s):
	res = []
	for i in range(len(s)):
		res.append(s[:i+1])

	return "".join(res)

s = "abc"
s = "Code"
print string_splosion(s)