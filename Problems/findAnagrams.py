
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

def findAnagrams(s, p):
	p_map = {}
	for char in p:
		if char not in p_map:
			p_map[char] = 1
		else:
			p_map[char] += 1
	
	count = len(p)
	res = []
	l = r = 0
	while r < len(s):
		if s[r] in p_map:
			p_map[s[r]] -= 1
			if p_map[s[r]] >= 0:
				count -= 1
		if count == 0:
			res.append(l)

		if r == l + len(p) - 1:
			if s[l] in p_map:
				if p_map[s[l]] >= 0:
					count += 1
				p_map[s[l]] += 1
			l += 1
		r += 1
	return res







s = "cbaebabacd"
p = "abc"
print findAnagrams(s, p)