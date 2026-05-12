class Solution:
    def areOccurrencesEqual(self, s):
        from collections import Counter
        freq = Counter(s)
        vals = set(freq.values())
        return len(vals) == 1
