count = 1
def palindromic_substring(s):
	if len(s) == 0:
		return 0

	for i in range(len(s))[:-1]:
		check_palindrome(i, i, s)
		check_palindrome(i, i+1, s)
	return count

def check_palindrome(l, r, s):
	global count
	while l >= 0 and r < len(s) and s[l] == s[r]:
		l -= 1
		r += 1
		count += 1

print palindromic_substring("aaa")