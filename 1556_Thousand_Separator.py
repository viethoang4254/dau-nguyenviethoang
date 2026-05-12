class Solution:
    def thousandSeparator(self, n):
        s = str(n)
        res = []
        count = 0
        for ch in reversed(s):
            if count and count % 3 == 0:
                res.append('.')
            res.append(ch)
            count += 1
        return "".join(reversed(res))
