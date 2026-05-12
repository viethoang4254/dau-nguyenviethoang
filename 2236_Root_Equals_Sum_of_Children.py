class Solution:
    def checkTree(self, root):
        if not root:
            return False
        return root.val == root.left.val + root.right.val
