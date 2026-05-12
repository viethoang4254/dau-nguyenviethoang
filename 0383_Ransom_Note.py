class Solution:
    def canConstruct(self, ransomNote, magazine):
        from collections import Counter
        need = Counter(ransomNote)
        have = Counter(magazine)
        for ch, cnt in need.items():
            if have[ch] < cnt:
                return False
        return True
