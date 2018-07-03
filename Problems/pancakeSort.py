def flip(arr, k):
	start = 0
	while start < k:
		temp = arr[start]
		arr[start] = arr[k]
		arr[k] = temp
		start += 1
		k -= 1

def find_max_idx(arr, k):
	idx = 0
	for i in range(k):
		if arr[i] > arr[idx]:
			idx = i
	return idx


def pancake_sort(arr):
  # flip_idx = len(arr) - 1
  # find max, set max = 5
  # flip max to front if idx != flip_idx
  # flip arr, max to end
  # flip_idx -= 1
  # 
  # until flip_idx == 0
  
  	flip_idx = len(arr)
	while flip_idx > 1:
		max_idx = find_max_idx(arr, flip_idx)
		if flip_idx - 1 != max_idx:
			flip(arr, max_idx)
			flip(arr, flip_idx - 1)
		flip_idx -= 1

	return arr

arr = [1, 5, 4, 3, 2]  
print pancake_sort(arr)