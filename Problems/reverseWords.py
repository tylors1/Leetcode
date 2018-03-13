def reverse_words(s):
	return " ".join([s[::-1] for s in s.split()])
	

print reverse_words("Let's take LeetCode contest")