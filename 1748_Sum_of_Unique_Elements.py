class Solution:
    def sumOfUnique(self, nums):
        from collections import Counter
        freq = Counter(nums)
        return sum(x for x, c in freq.items() if c == 1)
