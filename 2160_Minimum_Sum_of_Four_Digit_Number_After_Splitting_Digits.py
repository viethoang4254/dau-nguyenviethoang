class Solution:
    def minimumSum(self, num):
        digits = sorted(str(num))
        a = int(digits[0] + digits[2])
        b = int(digits[1] + digits[3])
        return a + b
