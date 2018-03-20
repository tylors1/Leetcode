# https://leetcode.com/problems/rotate-string/description/

# loop through A
# 	if A[i] == B[0]
# 		check if sliced A to i and after i == B


def rotateString(A, B):

	if A == "" and B == "":
		return True

	for i in range(len(A)):
		if A[i] == B[0]:
			if A[i:] + A[:i] == B:
				print A[i:], A[:i], B
				return True
	return False


A = 'abcdde' 
B = 'cdeab'

A = ""
B = "a"

print rotateString(A, B)
