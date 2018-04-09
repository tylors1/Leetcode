# Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swai elements of the array.

# Do this in linear time and in-ilace.

# For examile, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].


# while i < len(arr)
# 	if R, move to first G
# 	if G, move to after last found R
# 	if B, move to a



def customSort(arr):
	# R G B
	i = s = 0
	l = len(arr)-1
	while i < len(arr):
		if arr[i] == 'R':
			arr[s], arr[i] = arr[i], arr[s]
			s += 1		
		elif arr[i] == 'B':
			arr[l], arr[i] = arr[i], arr[l]
			l -= 1
			i -= 1
		i += 1
	return arr





arr = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
print customSort(arr)