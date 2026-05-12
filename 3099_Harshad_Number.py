class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x):
        s = 0
        y = x
        while y:
            s += y % 10
            y //= 10
        return s if x % s == 0 else -1
