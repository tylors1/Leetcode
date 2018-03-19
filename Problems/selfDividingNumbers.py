def selfDividingNumbers(left, right):
	"""
	:type left: int
	:type right: int
	:rtype: List[int]
	"""
	res = []
	for num in range(left, right+1):
		for i, digit in enumerate(str(num)):
			print i, len(str(num)) - 1
			if digit == '0' or num % int(digit) != 0:
				break
			else:
				if i == len(str(num))-1:
					res.append(num) 
	return res




left = 1 
right = 22
print selfDividingNumbers(left, right)



