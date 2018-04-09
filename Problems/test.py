
# def count(numbers, k):
# 	if k <= 1:
# 		return 0
# 	prod = 1
# 	res = 0
# 	left = 0

# 	for i in range(len(numbers)):
# 		prod = prod * numbers[i]
# 		while prod >= k:
# 			prod = prod / numbers[left]
# 			left += 1
# 		res += i - left + 1
# 	return res



# numbers = [1,2,3]
# k = 4
# # numbers = [4, 13, 20, 32, 44, 59, 61, 71, 75, 86, 88]
# # k = 567601

# print count(numbers, k)



def robber(elements):
	points = [0] * 100001
	curr = prev = 0
	for item in elements:
		points[item] += item
	for item in points:
		prev, curr = curr, max(prev + item, curr)
	return curr
	


elements = [1,2,1,3,2,3]
print robber(elements)



