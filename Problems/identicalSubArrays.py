# check if there are two subarrays in an array are identical



import pygtrie
def identical_subarray(arr1, arr2):
	large = small = []
	store = {}
	if len(arr1) <= len(arr2):
		small, large = arr1, arr2
	else:
		small, large = arr2, arr1

	for arr in small:
		if arr[0] not in store:
			store[arr[0]] = [arr[:]]
		else:
			store[arr[0]] += [arr[:]]

	print store
	for arr in large:
		print arr[0]
		if arr[0] in store:
			for sub in store[arr[0]]:
				print sub, arr
				if arr == sub:
					return True


	else:
		return False

def identical_subarray_trie(arr1, arr2):
	
	t = pygtrie.Trie()

	large = small = []
	if len(arr1) <= len(arr2):
		small, large = arr1, arr2
	else:
		small, large = arr2, arr1

	for item in small:
		print item
		t[item] = item

	print
	if t.values([1,2,3]):
		print
	


arr1 = [[9,5,4],[1,2,3],[2,6],[2,5]]
arr2 = [[5],[1,2],[6,7],[6,8]]

print identical_subarray_trie(arr1, arr2)


