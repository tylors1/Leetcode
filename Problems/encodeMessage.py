# Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.


def encode(s):
	curr = ""
	start = -1
	res = []
	for i in range(len(s)):
		if i == len(s)-1 or s[i] != s[i+1]:
			res.append(str(i-start))
			res.append(s[i])
			start = i
			curr = s[i]
	print res
	return ''.join(res)

def decode(s):
	res = []
	for i in range(len(s))[:-1:2]:
		res.append(s[i+1]*int(s[i]))
	return res

s = "AAAABBBCCDAA"
s = encode(s)
print s
print decode(s)