

def qs(arr, start, end):

	def partition(arr, start, end):
		i = start-1
		pivot = arr[end]

		for j in range(start, end):
			if arr[j] <= pivot:
				i += 1
				arr[i], arr[j] = arr[j], arr[i]
		arr[i+1], arr[end] = arr[end], arr[i+1]
		return i+1

	if start < end:
		p = partition(arr, start, end)

		qs(arr, start, p-1)
		qs(arr, p+1, end)




arr = [10,4,5,3,2,6,9]
qs(arr,0,len(arr)-1)
print arr