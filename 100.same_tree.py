# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q :
            return True

        if p and q and p.val == q.val:
            #checking if all the nodes are equal in both tree using a recursive function.
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

        return False
    

'''
js solution:
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    if (!p && !q)return true;
    if (p && q && p.val == q.val){
        return isSameTree(p.left,q.left) && isSameTree(p.right,q.right);
    }
    return false;
    
};
'''