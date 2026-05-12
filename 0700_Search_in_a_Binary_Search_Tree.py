class Solution:
    def searchBST(self, root, val):
        cur = root
        while cur:
            if cur.val == val:
                return cur
            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        return None
