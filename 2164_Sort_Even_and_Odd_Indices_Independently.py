class Solution:
    def sortEvenOdd(self, nums):
        even = sorted(nums[0::2])
        odd = sorted(nums[1::2], reverse=True)
        res = []
        ei = oi = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                res.append(even[ei])
                ei += 1
            else:
                res.append(odd[oi])
                oi += 1
        return res
