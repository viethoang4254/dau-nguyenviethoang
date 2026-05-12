class Solution:
    def selfDividingNumbers(self, left, right):
        res = []
        for x in range(left, right + 1):
            y = x
            ok = True
            while y > 0:
                d = y % 10
                if d == 0 or x % d != 0:
                    ok = False
                    break
                y //= 10
            if ok:
                res.append(x)
        return res
