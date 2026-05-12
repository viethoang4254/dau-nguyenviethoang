class Solution:
    def canAliceWin(self, nums):
        s1 = sum(x for x in nums if x < 10)
        s2 = sum(x for x in nums if x >= 10)
        return s1 != s2
