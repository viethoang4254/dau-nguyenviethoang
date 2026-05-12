class Solution:
    def mostCommonWord(self, paragraph, banned):
        banned_set = set(w.lower() for w in banned)
        word = []
        counts = {}
        for ch in paragraph + " ":
            if ch.isalpha():
                word.append(ch.lower())
            elif word:
                w = "".join(word)
                if w not in banned_set:
                    counts[w] = counts.get(w, 0) + 1
                word = []
        return max(counts, key=counts.get)
