# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa, 'ka', and 'ak'.



def decode(message):
	r1 = 1
	r2 = 1

	for i in range(1, len(message)):
		if message[i] == 0:
			r1 = 0

		if message[i - 1] == '1' or message[i-1] == '2' and message[i] <= '6':
			r1 = r2 + r1
			r2 = r1 - r2

		else:
			r2 = r1

	return r1




message = "124125"
message = "1161"
print decode(message)