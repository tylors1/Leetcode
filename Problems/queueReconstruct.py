# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


def reconstructQueue(people):
	# people.sort(key=lambda (h, k): (-h, k))
	people = sorted(people, key=lambda t: (t[0],t[1]))
	print people




print reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])