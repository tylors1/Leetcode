# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

class TrieNode:
	def __init__(self, value=None):
		self.value = value
		self.next = {}
		self.end = False

class Trie:

	def __init__(self):
		self.root = TrieNode()		

	def insert(self, word):
		# set current
		# loop through word
		# check if letter is in dict
			# if not add it
		# move to next letter in trie
		# enf of loop, set end of word

		current = self.root
		for i in range(0, len(word)):
			letter = word[i]
			if not letter in current.next:
				current[letter] = TrieNode(letter)
			current = current.next[letter]
		current.end = True

	def search(self, word):
		# set current
		# loop through word
			# check if letter in dict
				# if not, return None
			# set current to next
		# return current

		current = self.root
		for i in range(0, len(word)):
			letter = word[i]
			if not letter in current.next:
				return None
			current = current.next[letter]
		return current

	def traverse(self, node):
		results = []

		def dfs(current, path):
			if current == None:
				return
			if current.end:
				results.append(path)
			for key in current.next:
				defs(current.next[key], path + key)

		defs(node, '')
		return results

	def startswith(self, prefix):
		current = self.traverse(prefix)
		if not current:
			return []
		results = self.traverse(current)
		for i in range(0, len(results)):
			results[i] = prefix + results[i]
		return results



def prefixes(words, pre):
	for word in words:
		trie = Trie()
		trie.insert(word)
	return trie.startswith(pre)



words = ["dog", "deer", "deal"]
pre = "de"

print prefixes(words, pre)