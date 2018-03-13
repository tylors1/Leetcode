def plusOne(digits):

	for i in range(len(digits))[::-1]:
		if digits[i] < 9:
			digits[i] += 1
			return digits
		digits[i] = 0
	digits[0] = 1
	digits.append(0)

	return digits


digits = [1,2,3,9]
# digits = [1,2,3,4]
print plusOne(digits)