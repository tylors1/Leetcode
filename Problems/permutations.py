



def permute(s):
	arr = list(s)
	res = []
	def recurse(arr, l, r):
		if l == r:
			res.append(arr[:])
		else:
			for i in range(l, r):
				arr[l], arr[i] = arr[i], arr[l]
				recurse(arr, l+1, r)
				arr[l], arr[i] = arr[i], arr[l]


	recurse(arr, 0, len(arr))
	return res

s = "abc"
print permute(s)