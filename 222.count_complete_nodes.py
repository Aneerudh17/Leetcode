# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)

        if left_depth == right_depth:
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            return(1 << right_depth) + self.countNodes(root.left)

    def depth(self,node):
        depth = 0
        while node:
            depth += 1
            node = node.left
        return depth