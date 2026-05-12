class Solution:
    def isUnivalTree(self, root):
        if not root:
            return True
        val = root.val
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node.val != val:
                return False
            stack.append(node.left)
            stack.append(node.right)
        return True
