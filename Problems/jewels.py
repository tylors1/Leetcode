
J = "aA"
S = "aAAbbbb"

def jewels(J, S):
	count = 0 
	j_set = set([letter for letter in J])
	for char in S:
		if char in j_set:
			count += 1
	return count




print jewels(J, S)