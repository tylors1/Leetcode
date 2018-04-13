# Given two lowercase strings, sort S1 in same order as S2. If a char in S1 doesnt exist in S2, put them at the end. 
# S1 = "program"
# S2 = "grapo"
# res = "grrapom"



def sort_string(s1, s2):
	store = {}
	for char in s1:
		if char not in store:
			store[char] = 1
		else:
			store[char] += 1
	res = []
	end = []
	for char in s2:
		if char in store:
			res.append(char*store[char])
			store[char] = 0
	for char in store:
		if store[char] > 0:
			res.append(char*store[char])
	return "".join(res)


s1 = "program"
s2 = "grapo"
print sort_string(s1, s2)