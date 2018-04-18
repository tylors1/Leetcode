
def min_substring(s, target):

	chars = dict.fromkeys(target, 0)
	missing = len(target)
	start = end = 0
	res = s
	while end <= len(s):
		if s[end] in chars:				
			if missing > 0: 
				if s[end] in chars:
					if chars[s[end]] == 0:
						chars[s[end]] += 1
						missing -= 1
					else
						chars[s[end]] += 1
			else:
				s += 1






s = "BANCADEFABC"
target = "CAB"
min_substring(s, target)