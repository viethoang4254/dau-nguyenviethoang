class Solution:
    def guessNumber(self, n):
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            g = guess(m)
            if g == 0:
                return m
            if g < 0:
                r = m - 1
            else:
                l = m + 1
        return -1
