class Solution:
    def destCity(self, paths):
        starts = set(a for a, _ in paths)
        for _, b in paths:
            if b not in starts:
                return b
        return ""
