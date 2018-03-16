
def getIn(obj, arr):

	def traverse(obj, arr, i):
		if i == len(arr) - 1:
			return obj[arr[i]]
		if not obj:
			return None
		return traverse(obj[arr[i]], arr, i + 1)

	return traverse(obj, arr, 0)



obj = {"username": "sally", "profile": {"name": "Sally Clojurian", "address": {"city": "Austin", "state": "TX"}}}
arr = ["profile", "address", "city"]
print getIn(obj, arr)