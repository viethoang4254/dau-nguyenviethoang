class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        first = {}
        for i, v in enumerate(sorted_nums):
            if v not in first:
                first[v] = i
        return [first[v] for v in nums]
