def mySqrt(x):

	if x < 2:
		return x
  
	start = 1
	end = x   
	while (start <= end) :
		mid = (start + end) // 2
		 
		if (mid*mid == x) :
			return mid

		if x > mid*mid:
			start = mid + 1
			ans = mid
			 
		else :
			end = mid - 1
			 
	return ans

x = 6
print mySqrt(x)
			