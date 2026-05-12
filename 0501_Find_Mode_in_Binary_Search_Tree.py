class Solution:
    def findMode(self, root):
        stack = []
        cur = root
        prev = None
        count = 0
        best = 0
        res = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if prev is None or cur.val != prev:
                count = 1
            else:
                count += 1
            if count > best:
                best = count
                res = [cur.val]
            elif count == best:
                res.append(cur.val)
            prev = cur.val
            cur = cur.right
        return res
