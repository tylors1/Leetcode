# Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].



def find_words(lib, s):
	start = 0
	res = []
	for i in range(len(s)+1):
		print s[start:i]
		if s[start:i] in lib:
			res.append(s[start:i])
			start = i
	return res






lib = set(["quick", "brown", "the", "fox"])
s = "thequickbrownfox"
print find_words(lib, s)