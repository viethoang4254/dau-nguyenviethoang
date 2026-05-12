class Solution:
    def buildTree(self, preorder, inorder):
        idx = {v: i for i, v in enumerate(inorder)}
        pre_i = 0

        def build(lo, hi):
            nonlocal pre_i
            if lo > hi:
                return None
            root_val = preorder[pre_i]
            pre_i += 1
            root = TreeNode(root_val)
            mid = idx[root_val]
            root.left = build(lo, mid - 1)
            root.right = build(mid + 1, hi)
            return root

        return build(0, len(inorder) - 1)
