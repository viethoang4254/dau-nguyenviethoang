class Solution:
    def countEven(self, num):
        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s
        count = 0
        for x in range(1, num + 1):
            if digit_sum(x) % 2 == 0:
                count += 1
        return count
