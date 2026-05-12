class Solution:
    def mostFrequent(self, nums, key):
        counts = {}
        for i in range(len(nums) - 1):
            if nums[i] == key:
                nxt = nums[i + 1]
                counts[nxt] = counts.get(nxt, 0) + 1
        best = None
        best_count = -1
        for v, c in counts.items():
            if c > best_count:
                best_count = c
                best = v
        return best
