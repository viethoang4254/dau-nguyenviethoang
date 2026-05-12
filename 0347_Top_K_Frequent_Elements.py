class Solution:
    def topKFrequent(self, nums, k):
        from collections import Counter
        freq = Counter(nums)
        return [x for x, _ in freq.most_common(k)]
