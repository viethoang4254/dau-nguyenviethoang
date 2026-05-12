class Solution:
    def passThePillow(self, n, time):
        cycle = n - 1
        t = time % (2 * cycle)
        if t <= cycle:
            return 1 + t
        return n - (t - cycle)
