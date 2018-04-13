# https://techdevguide.withgoogle.com/paths/foundational/find-longest-word-in-dictionary-that-subsequence-of-given-string/#!

# For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"



from bisect import bisect_left
def find_longest_word(s, d):
	store = {}
	res = ""
	for i in range(len(s)):
		if s[i] not in store:
			store[s[i]] = [i]
		else:
			store[s[i]].append(i)
	for word in d:
		lower = 0
		flag = True
		for i in range(len(word)):
			if word[i] not in store:
				flag = False
				break
			idx = bisect_left(store[word[i]], lower)
			if idx == len(store[word[i]]):
				flag = False
				break
			lower = store[word[i]][idx] + 1
		if flag and len(word) > len(res):
			res = word
	return res






s = "abppplee"
d = ["able", "ale", "apple", "bale", "kangaroo"]

print find_longest_word(s, d)
