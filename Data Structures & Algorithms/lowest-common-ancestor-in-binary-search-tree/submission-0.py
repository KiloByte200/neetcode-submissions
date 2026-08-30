# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # recursive function
        # if no root return None
        # given some node
        # if q and p is < node -> return recursive function(node.left)
        # if q and p > node -> return recursive function(node.right)
        # else -> return node
        def search(node: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

            if q.val < node.val and p.val < node.val:
                return search(node.left, p, q)
            
            if q.val > node.val and p.val > node.val:
                return search(node.right, p, q)
            
            return node

        return search(root, p, q)

        
        