from heapq import heappush, heapify, nlargest
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap = []
        for item in nums:
            heappush(self.heap, item)
        self.k = k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heappush(self.heap, val)
        return nlargest(self.k, self.heap)[-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)