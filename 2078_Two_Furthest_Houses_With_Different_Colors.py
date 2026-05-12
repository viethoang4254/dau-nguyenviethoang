class Solution:
    def maxDistance(self, colors):
        n = len(colors)
        best = 0
        for i in range(n):
            if colors[i] != colors[0]:
                best = max(best, i)
            if colors[i] != colors[-1]:
                best = max(best, n - 1 - i)
        return best
