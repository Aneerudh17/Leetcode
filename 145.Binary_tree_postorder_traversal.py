# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #stack approach
        result = []

        def postorder(node):
            if not node:
                return []
            
            #visit left sub tree
            postorder(node.left)

            #visit right subtree
            postorder(node.right)

            #visit root after visiting children
            result.append(node.val)

        postorder(root)
        return result