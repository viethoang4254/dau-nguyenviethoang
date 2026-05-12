class Solution:
    def isHappy(self, n):
        def next_num(x):
            s = 0
            while x:
                s += (x % 10) ** 2
                x //= 10
            return s
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = next_num(n)
        return n == 1
