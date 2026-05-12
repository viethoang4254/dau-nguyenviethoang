class Solution:
    def numJewelsInStones(self, jewels, stones):
        jset = set(jewels)
        return sum(1 for ch in stones if ch in jset)
