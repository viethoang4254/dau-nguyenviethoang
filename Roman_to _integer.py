class Solution:
    def romanToInt(self, s):
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        
        for i in range(len(s)):
            cur = roman[s[i]]
            
            if i < len(s) - 1:
                next_val = roman[s[i + 1]]
                if cur < next_val:
                    total -= cur
                else:
                    total += cur
            else:
                total += cur
        
        return total
