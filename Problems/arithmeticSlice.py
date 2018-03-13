def arithmetic_slice(input_list):
	curr = 0
	res = 0

	for i in range(len(input_list))[2:]:
		if input_list[i-1]-input_list[i-2] == input_list[i] - input_list[i-1]:
			curr += 1
			res += curr
		else:
			curr = 0
	return res


print arithmetic_slice([2, 4, 6, 8, 10])
print arithmetic_slice([1, 3, 5, 7, 9])
print arithmetic_slice([1, 2, 3, 4])