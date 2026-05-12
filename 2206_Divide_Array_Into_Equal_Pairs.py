class Solution:
    def divideArray(self, nums):
        from collections import Counter
        freq = Counter(nums)
        return all(v % 2 == 0 for v in freq.values())
