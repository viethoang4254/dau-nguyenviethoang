class Solution:
    def targetIndices(self, nums, target):
        nums.sort()
        res = []
        for i, x in enumerate(nums):
            if x == target:
                res.append(i)
        return res
