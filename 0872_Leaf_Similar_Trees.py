class Solution:
    def leafSimilar(self, root1, root2):
        def leaves(root):
            res = []
            stack = [root]
            while stack:
                node = stack.pop()
                if not node:
                    continue
                if not node.left and not node.right:
                    res.append(node.val)
                else:
                    stack.append(node.right)
                    stack.append(node.left)
            return res
        return leaves(root1) == leaves(root2)
