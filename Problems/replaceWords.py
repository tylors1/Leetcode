




def replaceWords(dict, sentence):

	roots = set(dict)
	words = sentence.split()

	for i, word in enumerate(words):
		for j in range(len(word)):
			if word[:j] in roots:
				words[i] = word[:j]
				break

	return " ".join(words)

# dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"

dict = ["a", "aa", "aaa", "aaaa"]
sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"


print replaceWords(dict, sentence)