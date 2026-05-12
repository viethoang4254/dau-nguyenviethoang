class Solution:
    def largestAltitude(self, gain):
        cur = 0
        best = 0
        for x in gain:
            cur += x
            best = max(best, cur)
        return best
