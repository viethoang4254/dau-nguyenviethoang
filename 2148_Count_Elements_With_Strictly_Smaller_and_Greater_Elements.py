class Solution:
    def countElements(self, nums):
        if not nums:
            return 0
        mn = min(nums)
        mx = max(nums)
        return sum(1 for x in nums if mn < x < mx)
