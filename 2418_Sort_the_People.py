class Solution:
    def sortPeople(self, names, heights):
        pairs = sorted(zip(heights, names), reverse=True)
        return [name for _, name in pairs]
