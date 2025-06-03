# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def is_same(n1,n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False

            return n1.val == n2.val and is_same(n1.left,n2.right) and is_same(n1.right,n2.left)
        return is_same(root.left,root.right)

'''
javascript solution:
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function(root) {
    const is_same = (n1,n2) => {
        if (!n1 && !n2){
            return true;
        }
        if (!n1 || !n2){
            return false;
        }
        return n1.val === n2.val && is_same(n1.left,n2.right) && is_same(n1.right,n2.left);
    }
    return is_same(root.left,root.right);    
};
'''