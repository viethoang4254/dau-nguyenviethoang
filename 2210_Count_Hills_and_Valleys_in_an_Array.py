class Solution:
    def countHillValley(self, nums):
        filtered = [nums[0]]
        for x in nums[1:]:
            if x != filtered[-1]:
                filtered.append(x)
        count = 0
        for i in range(1, len(filtered) - 1):
            if filtered[i - 1] < filtered[i] > filtered[i + 1]:
                count += 1
            elif filtered[i - 1] > filtered[i] < filtered[i + 1]:
                count += 1
        return count
