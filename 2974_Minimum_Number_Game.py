class Solution:
    def numberGame(self, nums):
        nums.sort()
        res = []
        for i in range(0, len(nums), 2):
            res.append(nums[i + 1])
            res.append(nums[i])
        return res
