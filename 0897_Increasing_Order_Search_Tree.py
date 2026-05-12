class Solution:
    def increasingBST(self, root):
        dummy = TreeNode(0)
        cur = dummy
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.left = None
            cur.right = node
            cur = node
            node = node.right
        return dummy.right
