class Solution:
    def countBalls(self, lowLimit, highLimit):
        from collections import defaultdict
        boxes = defaultdict(int)
        best = 0
        for x in range(lowLimit, highLimit + 1):
            s = 0
            y = x
            while y:
                s += y % 10
                y //= 10
            boxes[s] += 1
            if boxes[s] > best:
                best = boxes[s]
        return best
