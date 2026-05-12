class Solution:
    def convertTime(self, current, correct):
        def to_min(t):
            h, m = t.split(':')
            return int(h) * 60 + int(m)
        cur = to_min(current)
        cor = to_min(correct)
        diff = cor - cur
        ops = 0
        for step in (60, 15, 5, 1):
            ops += diff // step
            diff %= step
        return ops
