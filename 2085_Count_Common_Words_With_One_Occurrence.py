class Solution:
    def countWords(self, words1, words2):
        from collections import Counter
        c1 = Counter(words1)
        c2 = Counter(words2)
        return sum(1 for w in c1 if c1[w] == 1 and c2.get(w, 0) == 1)
