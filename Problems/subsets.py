def subsets(nums):

    res = [[]]
    for num in sorted(nums):
    	print [item+[num] for item in res]
        res += [item+[num] for item in res]
        
    return res




nums = [1, 2, 3]
print subsets(nums)