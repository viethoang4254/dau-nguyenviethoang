class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        from collections import Counter
        ab = Counter()
        for a in nums1:
            for b in nums2:
                ab[a + b] += 1
        res = 0
        for c in nums3:
            for d in nums4:
                res += ab.get(-(c + d), 0)
        return res
