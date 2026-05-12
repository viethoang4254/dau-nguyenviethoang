class Solution:
    def digitSum(self, s, k):
        while len(s) > k:
            parts = []
            for i in range(0, len(s), k):
                chunk = s[i:i + k]
                parts.append(str(sum(int(ch) for ch in chunk)))
            s = "".join(parts)
        return s
