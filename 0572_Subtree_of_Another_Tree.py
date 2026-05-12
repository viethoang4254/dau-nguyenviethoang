class Solution:
    def isSubtree(self, root, subRoot):
        def same(a, b):
            if not a and not b:
                return True
            if not a or not b or a.val != b.val:
                return False
            return same(a.left, b.left) and same(a.right, b.right)

        def dfs(node):
            if not node:
                return False
            if same(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
