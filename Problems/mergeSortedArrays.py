def merge(arr1, arr2):

	p1 = 0
	p2 = 0
	res = []

	while True:
		if p1 >= len(arr1):
			return res + arr2[p2:]
		if p2 >= len(arr2):
			return res + arr1[p1:]
		if arr1[p1] < arr2[p2]:
			res.append(arr1[p1])
			p1 += 1
		else:
			res.append(arr2[p2])
			p2 += 1
		print res

	return res



arr1 = [1,3,5]
arr2 = [2,4,6,8,10]
print merge(arr1, arr2)