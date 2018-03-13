

def search(input, target):
	start = 0
	end = len(input)
	mid = None
	while start <= end:
		mid = (start + end) / 2
		if input[mid] == target:
			return mid
		if target < input[mid]:
			end = mid - 1
		else:
			start = mid + 1
	return -1


input = [1,3,4,5,6,7,8,10,11,13,15,17,20,22]
target = 17
print search(input, 17)