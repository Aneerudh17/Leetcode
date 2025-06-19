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
    
'''
js solution
var countNodes = function(root) {
  if (!root) return 0;

  const getDepth = (node) => {
    let depth = 0;
    while (node) {
      node = node.left;
      depth++;
    }
    return depth;
  };

  let leftDepth = getDepth(root.left);
  let rightDepth = getDepth(root.right);

  if (leftDepth === rightDepth) {
    return (1 << leftDepth) + countNodes(root.right);
  } else {
    return (1 << rightDepth) + countNodes(root.left);
  }
};
'''