class Solution:
    def heightChecker(self, heights):
        expected = sorted(heights)
        return sum(1 for a, b in zip(heights, expected) if a != b)
