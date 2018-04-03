# Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

# More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

# If you can only fit one word on a line, then you should pad the right-hand side with spaces.

# Each word is guaranteed not to be longer than k.

# For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly

# iterate over each word
# 	if len of word + 1 > k
# 		add new line to res:
			# from start to i-1, add k - total spaces
			# add new line to res
# 		reset total, line
# 	else
# 		add len of word + 1 to total



def justify(arr, k):
	res = []
	start = 0
	spaces = 0
	total = 0
	for i in range(len(arr)):
		if total + len(arr[i]) > k or i == len(arr)-1:
			if i == len(arr)-1:
				i+=1
				total += len(arr[i-1])
			spaces += k - total
			print total, spaces, arr[start:i]
			spaces_to_add = spaces / (i-start-1)
			extra = spaces % (i-start-1)
			print spaces_to_add, extra
			line = []
			for j in range(start, i):
				line.append(arr[j])
				print extra
				if j != i-1:
					line.append(" "*spaces_to_add)
					if extra > 0:
						extra -= 1
						line[-1] += " "
			res.append(''.join(line))
			total = 0
			start = i
			spaces = 0
		if i != len(arr):
			total += len(arr[i]) + 1
			spaces += 1
	return res


arr = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k = 16

print justify(arr, k)