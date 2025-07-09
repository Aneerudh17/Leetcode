# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []

        total = 0
        queue = [root]

        while queue:
            #dequeing the list
            node = queue.pop(0)

            if node.left:
                #if there is a left node then check if the node is a leaf node
                if not node.left.left and not node.left.right:
                    #if it is a leaf node then add the value to the total
                    total += node.left.val
                #if the left node is not a leaf node then just append it to the list for further iterations
                else:
                    queue.append(node.left)
            if node.right:
                #if the node is right node then add it to the queue for further iteration
                queue.append(node.right)
        return total