class Solution:
    def toGoatLatin(self, sentence):
        vowels = set("aeiouAEIOU")
        words = sentence.split()
        res = []
        for i, w in enumerate(words, 1):
            if w[0] in vowels:
                nw = w + "ma"
            else:
                nw = w[1:] + w[0] + "ma"
            nw += "a" * i
            res.append(nw)
        return " ".join(res)
