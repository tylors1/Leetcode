

def letter_case_permutation(S):

	l = len(S)
	r = []
	
	def backtrack(S, r, temp, first, last):    
		print temp
			
		for i in range(first,last):
			if S[i].isalpha(): # if current char is letter
				t_temp = temp +  S[i].lower()
				backtrack(S, r, t_temp, i+1, last) # original string, res array, new item, increase start idx, same last 
				t_temp = temp +  S[i].upper()
				backtrack(S, r, t_temp, i+1, last) # repeat for uppercase
				
			else:
				temp += S[i]

		if len(temp) == last: 
			r.append(temp)
			return r
		
		return r
	
	r =  backtrack(S, r, '', 0, l) # recurse

	if len(r) == 0:
		r.append(S)
	
	return r


S = "a1b2c3"
print letter_case_permutation(S)