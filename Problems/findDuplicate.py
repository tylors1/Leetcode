def find_duplicate(nums):

    slow = 0
    fast = 0


    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    finder = len(nums) - 1
    while True:
        slow   = nums[slow]
        finder = nums[finder]

        if slow == finder:
            return slow





# nums = [2,1,2]
# nums = [1,2,3,4,4,4,5]
nums = [1,1,2]
print find_duplicate(nums)