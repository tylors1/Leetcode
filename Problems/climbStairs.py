#  https://leetcode.com/problems/climbing-stairs/description/

# Input: 3
# Output:  3
# Explanation:  There are three ways to climb to the top.

# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step



def climb_stairs(n):
	a = 1
	b = 0
	for i in range(n):
		b, a = a, a + b
		print a, b
	return a



print climb_stairs(2)